mat1 = torch.randn(2, 3)
mat2 = torch.randn(3, 2)
output = torch.mm(mat1, mat2)
output = torch.mm(mat1, mat2, out=torch.empty(2, 2))