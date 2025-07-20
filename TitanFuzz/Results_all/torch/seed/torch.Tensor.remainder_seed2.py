input_tensor = torch.randn(10, 10)
divisor = torch.randn(10, 10)
output_tensor = torch.Tensor.remainder(input_tensor, divisor)