input_tensor = torch.randn(3, 3)
other = torch.randn(3, 3)
torch.Tensor.copysign_(input_tensor, other)