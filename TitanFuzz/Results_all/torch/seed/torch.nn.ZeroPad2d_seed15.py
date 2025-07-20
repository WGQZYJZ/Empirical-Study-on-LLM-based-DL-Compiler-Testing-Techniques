input = Variable(torch.ones(1, 1, 5, 5))
zero_padding = torch.nn.ZeroPad2d(2)
output = zero_padding(input)