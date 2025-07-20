input = torch.randn(10, 10)
alphaDropout = torch.nn.AlphaDropout(p=0.5, inplace=False)
output = alphaDropout(input)