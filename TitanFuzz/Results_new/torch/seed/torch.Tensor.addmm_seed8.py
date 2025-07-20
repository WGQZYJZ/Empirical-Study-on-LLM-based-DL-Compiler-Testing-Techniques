mat1 = torch.randn(5, 3)
mat2 = torch.randn(3, 4)
result = torch.Tensor.addmm(mat1, mat1, mat2, beta=0.5, alpha=0.5)