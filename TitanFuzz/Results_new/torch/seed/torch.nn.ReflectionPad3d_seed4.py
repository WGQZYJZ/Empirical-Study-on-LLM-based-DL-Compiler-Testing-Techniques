x = Variable(torch.ones(1, 1, 3, 3, 3))
pad = torch.nn.ReflectionPad3d(1)