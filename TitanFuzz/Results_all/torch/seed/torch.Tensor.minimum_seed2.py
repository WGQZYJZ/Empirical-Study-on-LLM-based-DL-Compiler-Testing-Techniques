input_tensor = torch.randn(1, 3)
other = torch.randn(1, 3)
minimum = torch.Tensor.minimum(input_tensor, other)