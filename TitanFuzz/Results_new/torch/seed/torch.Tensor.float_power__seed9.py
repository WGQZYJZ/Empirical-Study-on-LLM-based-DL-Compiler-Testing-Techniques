input_tensor = torch.randn(5, 5)
exponent = 2
torch.Tensor.float_power_(input_tensor, exponent)
input_tensor = torch.randn(5, 5)
other = torch.randn(5, 5)
torch.Tensor.fmod_(input_tensor, other)
input_tensor