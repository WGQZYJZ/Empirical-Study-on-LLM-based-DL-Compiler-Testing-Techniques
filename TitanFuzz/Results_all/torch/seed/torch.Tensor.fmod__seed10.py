input_tensor = torch.randn(1, 3, 3, 3)
divisor = torch.tensor([2, 2, 2], dtype=torch.float32)
torch.Tensor.fmod_(input_tensor, divisor)