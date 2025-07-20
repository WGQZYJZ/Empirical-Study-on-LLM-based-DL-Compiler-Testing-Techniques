input1 = torch.randn(2, 3)
input2 = torch.randn(2, 3)
bilinear = torch.nn.Bilinear(3, 3, 1)
output = bilinear(input1, input2)