input = torch.randn(1, 1, 3, 3)
upsample = torch.nn.UpsamplingBilinear2d(scale_factor=2)
output = upsample(input)