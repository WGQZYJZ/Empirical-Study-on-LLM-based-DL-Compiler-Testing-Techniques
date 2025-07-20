x = Variable(torch.ones(1, 1, 4, 4))
dropout = torch.nn.Dropout2d(p=0.5, inplace=False)
y = dropout(x)