input = Variable(torch.ones(1, 1, 4, 4))
padding = (1, 1, 1, 1)
output = torch.nn.ZeroPad2d(padding)(input)