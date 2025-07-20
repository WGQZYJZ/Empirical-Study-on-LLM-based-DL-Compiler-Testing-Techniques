input = torch.Tensor(1, 1, 4, 4, 4)
padding = (1, 1, 1, 1, 1, 1)
output = torch.nn.ReplicationPad3d(padding)(input)