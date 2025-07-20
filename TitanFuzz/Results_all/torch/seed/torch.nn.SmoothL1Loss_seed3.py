x = Variable(torch.randn(1, 1, 3, 3))
y = Variable(torch.randn(1, 1, 3, 3))
loss = torch.nn.SmoothL1Loss()