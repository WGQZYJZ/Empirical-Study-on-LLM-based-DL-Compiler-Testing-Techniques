x = torch.randn(100, 1000)
y = torch.nn.Dropout(p=0.5, inplace=False)(x)