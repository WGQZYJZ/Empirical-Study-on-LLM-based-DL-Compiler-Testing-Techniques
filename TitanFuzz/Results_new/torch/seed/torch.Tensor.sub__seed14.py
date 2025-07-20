input_tensor = torch.tensor([[1, 2, 3], [4, 5, 6]])
other = torch.tensor([[1, 1, 1], [1, 1, 1]])
output_tensor = torch.Tensor.sub_(input_tensor, other)
output_tensor = torch.Tensor.sub_(input_tensor, other, alpha=0.5)