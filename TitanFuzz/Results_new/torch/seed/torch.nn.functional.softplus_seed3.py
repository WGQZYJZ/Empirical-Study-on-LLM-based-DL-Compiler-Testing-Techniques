x = Variable(torch.randn(5, 5))
y = torch.nn.functional.softplus(x)