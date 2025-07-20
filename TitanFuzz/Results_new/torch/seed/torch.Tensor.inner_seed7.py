input_tensor = torch.randn(2, 3)
other = torch.randn(3, 2)
output = torch.Tensor.inner(input_tensor, other)