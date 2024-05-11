import csv


class VotingLogic:
    def __init__(self, ui):
        self.ui = ui
        self.voted_ids = set()
        self.jane_votes = 0
        self.john_votes = 0

        self.ui.SubmitButton.clicked.connect(self.cast_vote)

    def cast_vote(self):
        voter_id = self.ui.Id_lineEdit.text().strip()  # Ensure leading/trailing spaces are removed

        # Validate voter ID
        if not voter_id.isdigit() or len(voter_id) != 6:
            self.ui.results_label.setText("<font color='red'>ENTER VALID VOTER ID</font>")
            return

        if voter_id in self.voted_ids:
            self.ui.results_label.setText("<font color='red'>ALREADY VOTED</font>")
        else:
            candidate = "Jane" if self.ui.JaneButton.isChecked() else "John"
            self.voted_ids.add(voter_id)  # Add voter ID to prevent multiple votes
            self.save_vote(voter_id, candidate)
            self.update_vote_count(candidate)
        self.ui.Id_lineEdit.clear()
        self.ui.JaneButton.setChecked(False)
        self.ui.JohnButton.setChecked(False)

    def save_vote(self, voter_id, candidate):
        with open("voted_ids.csv", "a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([voter_id, candidate])

    def update_vote_count(self, candidate):
        if candidate == "Jane":
            self.jane_votes += 1
        elif candidate == "John":
            self.john_votes += 1

        # Update the results label to show the vote counts
        self.ui.results_label.setText(f"Vote submitted\nJane: {self.jane_votes} votes\nJohn: {self.john_votes} votes")