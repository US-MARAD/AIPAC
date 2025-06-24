from automation.fetch_aipac_donations import FECClient, save_to_csv
from unittest import mock


def test_fetch_disbursements_pagination(monkeypatch):
    responses = [
        {
            "results": [{"recipient_name": "A", "disbursement_amount": 1}],
            "pagination": {"page": 1, "pages": 2},
        },
        {
            "results": [{"recipient_name": "B", "disbursement_amount": 2}],
            "pagination": {"page": 2, "pages": 2},
        },
    ]

    def fake_get(url, params=None, timeout=None):
        index = params.get("page") - 1
        response = mock.Mock()
        response.json.return_value = responses[index]
        response.raise_for_status.return_value = None
        return response

    monkeypatch.setattr("requests.get", fake_get)
    client = FECClient("TEST")
    records = list(client.fetch_disbursements(2022))
    assert len(records) == 2
    assert records[0]["recipient_name"] == "A"
    assert records[1]["recipient_name"] == "B"


def test_save_to_csv(tmp_path):
    data = [
        {
            "recipient_committee_name": "COM",
            "recipient_name": "A",
            "disbursement_date": "2022-01-01",
            "disbursement_amount": 10,
        }
    ]
    path = tmp_path / "out.csv"
    save_to_csv(iter(data), path)
    text = path.read_text()
    assert "recipient_name" in text
    assert "A" in text
