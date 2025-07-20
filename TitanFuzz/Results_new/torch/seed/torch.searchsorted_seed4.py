sorted_sequence = torch.tensor([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
values = torch.tensor([2, 4, 6, 8, 10])
out = torch.searchsorted(sorted_sequence, values, right=False)