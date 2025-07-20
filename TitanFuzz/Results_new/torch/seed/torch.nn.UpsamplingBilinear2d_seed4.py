input = torch.randn(1, 1, 5, 5)
input = torch.randn(1, 1, 5, 5)
upsample = torch.nn.UpsamplingBilinear2d(scale_factor=2)
output = upsample(input)