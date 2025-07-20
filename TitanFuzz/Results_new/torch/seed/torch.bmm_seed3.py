input = torch.randn(10, 3, 4)
mat2 = torch.randn(10, 4, 5)
out = torch.bmm(input, mat2)