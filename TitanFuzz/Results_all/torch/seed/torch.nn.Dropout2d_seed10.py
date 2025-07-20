x = Variable(torch.randn(10, 10))
dropout = torch.nn.Dropout2d(p=0.5, inplace=False)
y = dropout(x)