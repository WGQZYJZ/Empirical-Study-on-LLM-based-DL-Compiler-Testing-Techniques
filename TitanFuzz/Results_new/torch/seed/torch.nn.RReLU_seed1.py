x = torch.randn(1, 1, 3, 3)
rrelu = torch.nn.RReLU(lower=0.125, upper=0.3333333333333333, inplace=False)
y = rrelu(x)