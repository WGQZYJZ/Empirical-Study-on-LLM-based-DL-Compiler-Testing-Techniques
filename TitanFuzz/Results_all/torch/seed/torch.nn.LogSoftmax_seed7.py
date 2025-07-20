input = torch.randn(2, 3)
output = torch.nn.LogSoftmax(dim=1)(input)