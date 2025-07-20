input_tensor = torch.randn(4, 4)
other = torch.randn(4, 4)
result = torch.Tensor.less_equal_(input_tensor, other)