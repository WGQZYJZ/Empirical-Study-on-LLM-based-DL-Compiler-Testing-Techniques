input = torch.randn(1, 1, 5, 5)
output = torch.nn.functional.upsample_bilinear(input, size=None, scale_factor=2)