input_tensor = torch.randn(4, 4)
other_tensor = torch.randn(4, 4)
result = torch.Tensor.sub_(input_tensor, other_tensor)