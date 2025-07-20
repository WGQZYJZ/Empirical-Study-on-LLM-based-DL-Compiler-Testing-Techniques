input_tensor = torch.randn(5, 3)
other = torch.randn(5, 3)
output = torch.Tensor.ne_(input_tensor, other)