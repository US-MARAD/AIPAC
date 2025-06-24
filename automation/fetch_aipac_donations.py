"""Fetch AIPAC PAC donations to congressional candidates from the FEC API."""

import csv
import os
import requests
from datetime import datetime
from typing import Iterator, Dict

FEC_ENDPOINT = "https://api.open.fec.gov/v1/schedules/schedule_b/"
COMMITTEE_ID = "C00797670"  # AIPAC PAC


class FECClient:
    """Simple client for the FEC API."""

    def __init__(self, api_key: str) -> None:
        self.api_key = api_key

    def fetch_disbursements(self, cycle: int) -> Iterator[Dict[str, str]]:
        """Yield disbursements for the given cycle."""
        page = 1
        params = {
            "api_key": self.api_key,
            "committee_id": COMMITTEE_ID,
            "two_year_transaction_period": cycle,
            "per_page": 100,
        }
        while True:
            params["page"] = page
            resp = requests.get(FEC_ENDPOINT, params=params, timeout=30)
            resp.raise_for_status()
            data = resp.json()
            for item in data.get("results", []):
                yield {
                    "recipient_committee_name": item.get("recipient_committee_name"),
                    "recipient_name": item.get("recipient_name"),
                    "disbursement_date": item.get("disbursement_date"),
                    "disbursement_amount": item.get("disbursement_amount"),
                }
            pagination = data.get("pagination", {})
            if page >= pagination.get("pages", 0):
                break
            page += 1


def save_to_csv(records: Iterator[Dict[str, str]], path: str) -> None:
    """Save disbursement records to CSV."""
    with open(path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(
            f,
            fieldnames=[
                "recipient_committee_name",
                "recipient_name",
                "disbursement_date",
                "disbursement_amount",
            ],
        )
        writer.writeheader()
        for row in records:
            writer.writerow(row)


def main() -> None:
    api_key = os.environ.get("FEC_API_KEY")
    if not api_key:
        raise SystemExit("FEC_API_KEY environment variable not set")
    cycle = 2022
    client = FECClient(api_key)
    records = client.fetch_disbursements(cycle)
    output_dir = os.path.join("data", "raw")
    os.makedirs(output_dir, exist_ok=True)
    timestamp = datetime.utcnow().strftime("%Y%m%d%H%M%S")
    output_path = os.path.join(
        output_dir,
        f"aipac_donations_{cycle}_{timestamp}.csv",
    )
    save_to_csv(records, output_path)
    print(f"Saved data to {output_path}")


if __name__ == "__main__":
    main()
