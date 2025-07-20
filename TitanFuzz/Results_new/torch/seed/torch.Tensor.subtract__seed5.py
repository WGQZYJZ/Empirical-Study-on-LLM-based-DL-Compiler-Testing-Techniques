input_tensor = torch.rand(2, 3)
other = torch.rand(2, 3)
result = torch.Tensor.subtract_(input_tensor, other)