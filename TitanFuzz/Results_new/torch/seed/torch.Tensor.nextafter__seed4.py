input_tensor = torch.randn(2, 3)
other_tensor = torch.randn(2, 3)
result = torch.Tensor.nextafter_(input_tensor, other_tensor)