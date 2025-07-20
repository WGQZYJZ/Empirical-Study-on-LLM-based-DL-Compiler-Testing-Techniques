input_tensor = torch.tensor([[1, 2, 3], [4, 5, 6]])
output_tensor = torch.Tensor.resize_as_(input_tensor, torch.tensor([[1, 2, 3], [4, 5, 6]]))