input = Variable(torch.randn(1, 1, 10, 10, 10))
output = torch.nn.functional.dropout3d(input, p=0.5, training=True, inplace=False)