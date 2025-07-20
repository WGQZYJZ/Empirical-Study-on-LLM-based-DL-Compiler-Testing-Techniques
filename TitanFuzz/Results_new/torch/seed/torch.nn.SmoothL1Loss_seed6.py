x = Variable(torch.randn(10, 3), requires_grad=True)
y = Variable(torch.randn(10, 3), requires_grad=True)
criterion = torch.nn.SmoothL1Loss()
loss = criterion(x, y)