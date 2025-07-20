sorted_sequence = torch.tensor([1, 3, 5, 7, 9], dtype=torch.float32)
values = torch.tensor([0, 2, 4, 6, 8, 10], dtype=torch.float32)
torch.searchsorted(sorted_sequence, values, right=True)