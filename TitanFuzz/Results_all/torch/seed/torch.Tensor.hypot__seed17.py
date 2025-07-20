input_tensor = torch.rand(4, 4)
other = torch.rand(4, 4)
result = torch.Tensor.hypot_(input_tensor, other)