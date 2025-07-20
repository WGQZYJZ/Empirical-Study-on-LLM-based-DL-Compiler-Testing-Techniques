input = Variable(torch.randn(2, 3, 4, 5, 6))
output = torch.nn.functional.dropout3d(input, p=0.5, training=True, inplace=False)