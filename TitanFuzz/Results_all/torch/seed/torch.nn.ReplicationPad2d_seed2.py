input = Variable(torch.randn(1, 1, 4, 4))
padding = 1
output = torch.nn.ReplicationPad2d(padding)(input)