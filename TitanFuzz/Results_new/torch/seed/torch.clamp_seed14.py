input_data = torch.randn(5)
output_data = torch.clamp(input_data, min=(- 0.5), max=0.5)