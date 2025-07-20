input_tensor = torch.randn(2, 3)
other = torch.randn(2, 3)
result = torch.Tensor.logaddexp(input_tensor, other)
result = torch.logaddexp(input_tensor, other)