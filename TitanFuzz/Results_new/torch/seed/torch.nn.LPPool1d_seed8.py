input = Variable(torch.randn(1, 3, 5))
pooling = torch.nn.LPPool1d(1, 3, stride=2)
output = pooling(input)