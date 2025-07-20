input_tensor = torch.randn(10)
torch.Tensor.clamp_(input_tensor, min=(- 0.5), max=0.5)