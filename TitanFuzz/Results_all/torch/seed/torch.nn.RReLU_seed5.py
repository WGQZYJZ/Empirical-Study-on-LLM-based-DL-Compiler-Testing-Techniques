x = torch.randn(1, 1, 10, 10)
x = Variable(x)
relu = torch.nn.RReLU(lower=0.125, upper=0.3333333333333333, inplace=False)
out = relu(x)