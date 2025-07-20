input_tensor = torch.randn(3, 5)
output_tensor = torch.median(input_tensor, dim=(- 1))