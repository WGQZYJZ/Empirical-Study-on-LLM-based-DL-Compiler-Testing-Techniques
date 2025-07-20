input_tensor = torch.randn(5, 3)
other = torch.randn(5, 3)
output_tensor = torch.Tensor.less_equal_(input_tensor, other)