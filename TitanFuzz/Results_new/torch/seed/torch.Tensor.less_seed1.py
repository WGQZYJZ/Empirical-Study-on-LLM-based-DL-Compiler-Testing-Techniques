input_tensor = torch.randn(1, 3, 4, 5)
other = torch.randn(1, 3, 4, 5)
result = torch.Tensor.less(input_tensor, other)