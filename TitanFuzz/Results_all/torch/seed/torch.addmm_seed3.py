mat1 = torch.ones(10, 10)
mat2 = torch.ones(10, 10)
mat3 = torch.ones(10, 10)
torch.addmm(mat1, mat2, mat3)