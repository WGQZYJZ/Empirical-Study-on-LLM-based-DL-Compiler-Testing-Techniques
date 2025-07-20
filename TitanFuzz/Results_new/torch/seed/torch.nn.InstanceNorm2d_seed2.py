x = Variable(torch.randn(1, 3, 3, 3))
x = Variable(torch.randn(1, 3, 3, 3))
y = torch.nn.InstanceNorm2d(3, affine=False)(x)