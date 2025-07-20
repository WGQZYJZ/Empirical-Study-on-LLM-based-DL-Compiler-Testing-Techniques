input_tensor = torch.randn(4, 4)
clamped_tensor = torch.clamp(input_tensor, min=(- 0.5), max=0.5)