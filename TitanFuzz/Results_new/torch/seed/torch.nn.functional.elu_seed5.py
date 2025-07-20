x = Variable(torch.randn(2, 3))
y = torch.nn.functional.elu(x, alpha=1.0, inplace=False)