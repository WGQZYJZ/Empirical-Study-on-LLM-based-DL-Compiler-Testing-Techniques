input_data = torch.randn(2, 3)
clamped_data = torch.clamp(input_data, min=(- 0.5), max=0.5)