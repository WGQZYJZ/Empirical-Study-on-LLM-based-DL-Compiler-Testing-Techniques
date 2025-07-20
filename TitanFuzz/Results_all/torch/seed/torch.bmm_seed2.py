batch = 2
input = torch.randn(batch, 3, 4)
mat2 = torch.randn(batch, 4, 5)
output = torch.bmm(input, mat2)
output = torch.bmm(input, mat2, out=torch.zeros(batch, 3, 5))