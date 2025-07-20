input = torch.randn(1, 1, 3, 3)
padding = (1, 2, 1, 2)
output = torch.nn.ReplicationPad2d(padding)(input)