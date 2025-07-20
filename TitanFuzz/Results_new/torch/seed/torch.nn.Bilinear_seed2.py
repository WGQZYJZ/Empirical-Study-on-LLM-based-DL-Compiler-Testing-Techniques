input1 = Variable(torch.randn(2, 3))
input2 = Variable(torch.randn(2, 3))
bilinear = torch.nn.Bilinear(3, 3, 1)
output = bilinear(input1, input2)