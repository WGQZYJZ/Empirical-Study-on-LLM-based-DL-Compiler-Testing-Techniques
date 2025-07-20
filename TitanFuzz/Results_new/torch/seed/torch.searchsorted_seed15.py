sorted_sequence = torch.arange(0, 10, 2)
values = torch.tensor([1, 2, 4, 5, 6, 8, 9])
result = torch.searchsorted(sorted_sequence, values)
result = torch.searchsorted(sorted_sequence, values, right=True)