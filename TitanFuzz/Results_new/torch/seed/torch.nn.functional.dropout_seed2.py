x = Variable(torch.ones(2, 2))
y = torch.nn.functional.dropout(x, p=0.5, training=True, inplace=False)