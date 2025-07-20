input_tensor = torch.rand(5, 5)
other = torch.rand(5, 5)
output = torch.Tensor.hypot_(input_tensor, other)