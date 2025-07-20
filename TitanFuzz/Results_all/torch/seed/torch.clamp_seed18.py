input_data = torch.randn(1, 3)
output_data = torch.clamp(input_data, min=0.5, max=1.5)