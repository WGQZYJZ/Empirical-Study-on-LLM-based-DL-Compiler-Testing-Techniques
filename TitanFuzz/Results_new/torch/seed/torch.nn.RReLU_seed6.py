x = torch.randn(1, requires_grad=True)
relu = torch.nn.RReLU(lower=0.125, upper=0.3333333333333333, inplace=False)