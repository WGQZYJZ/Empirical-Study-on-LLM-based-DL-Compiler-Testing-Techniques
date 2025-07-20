input_tensor = torch.tensor([[1, 2, 3], [4, 5, 6]])
other = torch.tensor([1, 2, 3])
output = torch.Tensor.not_equal_(input_tensor, other)