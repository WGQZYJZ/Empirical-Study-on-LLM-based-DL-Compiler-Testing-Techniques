x = Variable(torch.randn(1, 1, 3, 3))
dropout2d = torch.nn.functional.dropout2d(x, p=0.5, training=True, inplace=False)
dropout2d = torch.nn.functional.dropout2d(x, p=0.5, training=False, inplace=False)