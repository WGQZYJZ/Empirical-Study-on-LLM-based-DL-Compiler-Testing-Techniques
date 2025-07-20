input = Variable(torch.ones(1, 1, 2, 2, 2))
output = torch.nn.Dropout3d(p=0.5, inplace=False)(input)