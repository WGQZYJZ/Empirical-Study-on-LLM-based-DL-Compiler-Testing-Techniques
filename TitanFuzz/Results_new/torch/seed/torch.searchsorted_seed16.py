sorted_sequence = torch.tensor([1, 2, 3, 4, 5, 6, 7, 8, 9])
values = torch.tensor([3, 2, 4, 5, 1, 8, 7, 6, 9])
torch.searchsorted(sorted_sequence, values, out_int32=False, right=False, out=None)