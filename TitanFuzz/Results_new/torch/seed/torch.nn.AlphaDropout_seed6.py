x = torch.randn(2, 2)
dropout = torch.nn.AlphaDropout(p=0.5, inplace=False)
y = dropout(x)