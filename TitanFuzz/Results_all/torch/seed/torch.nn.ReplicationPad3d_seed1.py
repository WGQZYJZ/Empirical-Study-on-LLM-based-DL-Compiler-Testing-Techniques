input = Variable(torch.ones(1, 1, 3, 3, 3))
output = torch.nn.ReplicationPad3d(padding=(1, 1, 1, 1, 1, 1))(input)