input = Variable(torch.randn(5, 5))
dropout = torch.nn.AlphaDropout(p=0.5, inplace=False)
output = dropout(input)