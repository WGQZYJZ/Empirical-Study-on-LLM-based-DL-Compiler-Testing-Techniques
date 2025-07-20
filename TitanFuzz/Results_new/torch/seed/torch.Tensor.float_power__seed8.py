input_tensor = torch.randn(3, 3)
exponent = torch.randint(1, 5, (3, 3))
result = torch.Tensor.float_power_(input_tensor, exponent)