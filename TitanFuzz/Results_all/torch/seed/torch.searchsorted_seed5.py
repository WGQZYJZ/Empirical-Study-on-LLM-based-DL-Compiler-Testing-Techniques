sorted_sequence = torch.arange(10, dtype=torch.float)
values = torch.tensor([0.1, 1.2, 5.4, 9.1])
output = torch.searchsorted(sorted_sequence, values)
output = torch.searchsorted(sorted_sequence, values, right=True)