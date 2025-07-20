input = Variable(torch.randn(1, 1, 3, 3))
output = torch.nn.functional.upsample_bilinear(input, size=None, scale_factor=2)
input = Variable(torch.randn(1, 1, 3, 3))