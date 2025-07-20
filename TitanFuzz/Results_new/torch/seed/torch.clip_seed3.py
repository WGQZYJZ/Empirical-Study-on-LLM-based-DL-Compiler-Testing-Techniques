input_data = torch.randn(1, 3)
output_data = torch.clip(input_data, min=(- 0.5), max=0.5)
input_data = torch.randn(1, 3)
output_data = torch.clamp(input_data, min=(- 0.5), max=0.5)