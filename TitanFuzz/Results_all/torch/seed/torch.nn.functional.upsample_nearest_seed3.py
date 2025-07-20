input = Variable(torch.randn(1, 1, 3, 3))
output = torch.nn.functional.upsample_nearest(input, size=None, scale_factor=2)