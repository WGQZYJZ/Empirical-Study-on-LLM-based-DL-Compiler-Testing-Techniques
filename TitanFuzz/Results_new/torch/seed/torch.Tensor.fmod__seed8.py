input_tensor = torch.randn(3, 3)
divisor = torch.randn(3, 3)
torch.Tensor.fmod_(input_tensor, divisor)