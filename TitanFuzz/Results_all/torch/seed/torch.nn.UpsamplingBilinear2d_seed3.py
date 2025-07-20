input = Variable(torch.randn(1, 1, 5, 5))
upsample_bilinear = torch.nn.UpsamplingBilinear2d(size=None, scale_factor=2)
output = upsample_bilinear(input)