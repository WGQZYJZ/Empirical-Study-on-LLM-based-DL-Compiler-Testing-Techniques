input = torch.randn(2, 3, 4)
size = (2, 2, 2)
stride = (3, 2, 1)
output = torch.as_strided(input, size, stride)