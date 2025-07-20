mat1 = torch.randn(3, 4)
mat2 = torch.randn(4, 3)
torch.Tensor.addmm_(mat1, mat1, mat2, beta=1, alpha=1)