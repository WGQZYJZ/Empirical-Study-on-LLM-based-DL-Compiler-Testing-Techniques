input_tensor = torch.randn(3, 3, requires_grad=True)
output_tensor = torch.Tensor.float_power_(input_tensor, exponent=2)