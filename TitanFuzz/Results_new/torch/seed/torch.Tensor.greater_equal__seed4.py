input_tensor = torch.randn(3, 3)
other_tensor = torch.randn(3, 3)
result_tensor = torch.Tensor.greater_equal_(input_tensor, other_tensor)