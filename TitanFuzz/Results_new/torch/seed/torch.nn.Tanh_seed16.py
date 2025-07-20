x = Variable(torch.randn(5, 3))
y = torch.nn.Tanh()
z = y(x)