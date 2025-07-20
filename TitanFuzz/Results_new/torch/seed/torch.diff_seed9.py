input_data = torch.tensor([[1, 2, 3], [4, 5, 6]])
output_data = torch.diff(input_data, n=1, dim=(- 1), prepend=None, append=None)