x = Variable(torch.ones(2, 2))
y = torch.nn.Dropout(p=0.5)
z = y(x)