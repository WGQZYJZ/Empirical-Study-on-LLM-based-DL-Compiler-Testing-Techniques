input_tensor = torch.randn(4, 4)
divisor = torch.randn(4, 4)
output_tensor = torch.Tensor.fmod_(input_tensor, divisor)