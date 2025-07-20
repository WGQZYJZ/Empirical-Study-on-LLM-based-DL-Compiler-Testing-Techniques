input_tensor = torch.tensor([[1, 2, 3], [4, 5, 6]])
output = torch.Tensor.not_equal_(input_tensor, torch.tensor([[1, 2, 3], [4, 5, 6]]))