input = Variable(torch.rand(4, 4))
other = Variable(torch.rand(4, 4))
output = torch.special.gammaincc(input, other)