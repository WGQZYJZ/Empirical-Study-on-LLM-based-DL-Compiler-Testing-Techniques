input_tensor = torch.randn(1, 3, 3)
other = torch.randn(1, 3, 3)
result = torch.Tensor.less_equal(input_tensor, other)