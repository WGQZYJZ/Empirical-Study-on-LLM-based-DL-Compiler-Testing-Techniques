input_tensor = torch.Tensor([[1, 2, 3], [4, 5, 6]])
other = torch.Tensor([[1, 1, 1], [1, 1, 1]])
output = torch.Tensor.gt_(input_tensor, other)