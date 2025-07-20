x = Variable(torch.randn(5, 5))
dropout2d = torch.nn.Dropout2d(p=0.5, inplace=False)
y = dropout2d(x)