input_tensor = torch.randn(5, 3)
other_tensor = torch.randn(5, 3)
result = torch.Tensor.add_(input_tensor, other_tensor)