input = torch.rand(1, 1, 2, 2, 2)
replicationPad3d = torch.nn.ReplicationPad3d((1, 1, 1, 1, 1, 1))
output = replicationPad3d(input)