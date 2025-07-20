input = Variable(torch.Tensor(1, 1, 4, 4, 4))
torch.nn.ReplicationPad3d(padding=1)(input)