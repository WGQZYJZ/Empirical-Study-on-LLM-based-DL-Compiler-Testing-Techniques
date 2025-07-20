input = Variable(torch.randn(4, 4))
other = Variable(torch.randn(4, 4))
output = torch.special.gammaincc(input, other)