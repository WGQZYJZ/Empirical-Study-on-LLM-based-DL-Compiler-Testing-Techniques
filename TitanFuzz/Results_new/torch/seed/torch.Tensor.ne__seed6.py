input_tensor = torch.tensor([[1, 2], [3, 4]])
other = torch.tensor([[1, 2], [3, 4]])
output_tensor = torch.Tensor.ne_(input_tensor, other)