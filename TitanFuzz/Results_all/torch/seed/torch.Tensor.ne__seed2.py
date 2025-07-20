input_tensor = torch.randn(5, 3)
result = torch.Tensor.ne_(input_tensor, 3)
other_tensor = torch.randn(5, 3)
result = torch.Tensor.ne_(input_tensor, other_tensor)