input_tensor = torch.randn(3, 3)
divisor = 2
torch.Tensor.fmod_(input_tensor, divisor)