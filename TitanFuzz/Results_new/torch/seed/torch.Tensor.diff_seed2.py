input_tensor = torch.tensor([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15]])
output_tensor = torch.Tensor.diff(input_tensor, n=1, dim=(- 1), prepend=None, append=None)