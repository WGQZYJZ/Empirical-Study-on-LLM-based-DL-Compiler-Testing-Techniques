input = Variable(torch.randn(1, 3, 5, 5))
upsample_bilinear = torch.nn.functional.upsample_bilinear(input, size=None, scale_factor=2)
upsample_nearest = torch.nn.functional.upsample_nearest(input, size=None, scale_factor=2)