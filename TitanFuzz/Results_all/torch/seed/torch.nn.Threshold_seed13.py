x = Variable(torch.randn(2, 3), requires_grad=True)
y = torch.nn.Threshold(0.5, 0)(x)