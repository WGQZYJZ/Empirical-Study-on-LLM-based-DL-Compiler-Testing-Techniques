sorted_sequence = torch.tensor([1, 2, 3, 4, 5])
values = torch.tensor([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
result = torch.searchsorted(sorted_sequence, values, right=True)
result = torch.searchsorted(sorted_sequence, values, right=False)