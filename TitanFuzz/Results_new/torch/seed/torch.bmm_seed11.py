mat1 = torch.rand((4, 3, 2))
mat2 = torch.rand((4, 2, 3))
torch.bmm(mat1, mat2)