input = Variable(torch.randn(5, 5, 5))
dropout3d = torch.nn.Dropout3d(p=0.5, inplace=False)
output = dropout3d(input)