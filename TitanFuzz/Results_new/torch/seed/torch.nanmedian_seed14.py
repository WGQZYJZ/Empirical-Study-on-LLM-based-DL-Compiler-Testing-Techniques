input_data = torch.tensor([[1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4]])
output = torch.nanmedian(input_data, dim=0, keepdim=False, out=None)