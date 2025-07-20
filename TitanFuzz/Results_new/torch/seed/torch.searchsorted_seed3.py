in_data = torch.tensor([1, 2, 3, 4, 5, 6, 7], dtype=torch.float32)
search_data = torch.tensor([2, 4, 6, 8], dtype=torch.float32)
result = torch.searchsorted(in_data, search_data, out_int32=False, right=False)