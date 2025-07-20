x = Variable(torch.randn(1, 1, 3, 3))
y = torch.nn.functional.upsample(x, scale_factor=2, mode='bilinear')