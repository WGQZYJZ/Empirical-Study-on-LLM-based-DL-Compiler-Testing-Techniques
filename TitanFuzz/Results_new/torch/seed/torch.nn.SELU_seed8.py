x = Variable(torch.randn(2, 2))
selu = torch.nn.SELU(inplace=False)
y = selu(x)