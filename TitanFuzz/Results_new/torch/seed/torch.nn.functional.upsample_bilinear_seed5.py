input_data = torch.randn(1, 1, 6, 6)
output = torch.nn.functional.upsample_bilinear(input_data, scale_factor=2)
output = torch.nn.functional.upsample_bilinear(input_data, size=12)