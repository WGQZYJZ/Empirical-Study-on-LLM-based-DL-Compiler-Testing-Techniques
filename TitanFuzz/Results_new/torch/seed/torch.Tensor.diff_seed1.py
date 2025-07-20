input_tensor = torch.tensor([[1, 2, 3, 4, 5, 6, 7], [1, 2, 3, 4, 5, 6, 7]])
result = torch.Tensor.diff(input_tensor, n=1, dim=(- 1), prepend=None, append=None)