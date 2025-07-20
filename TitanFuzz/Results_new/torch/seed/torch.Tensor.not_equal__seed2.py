input_tensor = torch.Tensor([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
other = torch.Tensor([[1, 1, 1], [1, 1, 1], [1, 1, 1]])
result = torch.Tensor.not_equal_(input_tensor, other)