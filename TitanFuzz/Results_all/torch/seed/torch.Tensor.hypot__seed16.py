input_data = torch.randn(2, 3)
other = torch.randn(2, 3)
output = torch.Tensor.hypot_(input_data, other)