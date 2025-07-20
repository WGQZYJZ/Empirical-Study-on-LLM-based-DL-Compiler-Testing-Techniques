mat1 = torch.randn(2, 3)
mat2 = torch.randn(3, 4)
torch.Tensor.addmm_(mat1, mat1, mat2)