input = torch.rand(1, 1, 3, 3)
upsample = torch.nn.UpsamplingBilinear2d(size=(3, 3))
output = upsample(input)