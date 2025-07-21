x = Variable(torch.randn(2, 3), requires_grad=True)
y = Variable(torch.randn(2, 3), requires_grad=True)
loss = torch.nn.SmoothL1Loss()