x = Variable(torch.randn(5, 5))
y = Variable(torch.randn(5, 5))
z = torch.nn.functional.hardswish(x, inplace=False)