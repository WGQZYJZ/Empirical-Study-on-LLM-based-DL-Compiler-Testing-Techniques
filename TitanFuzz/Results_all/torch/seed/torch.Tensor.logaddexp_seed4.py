input_tensor = torch.randn(3, 3)
other = torch.randn(3, 3)
result = torch.Tensor.logaddexp(input_tensor, other)