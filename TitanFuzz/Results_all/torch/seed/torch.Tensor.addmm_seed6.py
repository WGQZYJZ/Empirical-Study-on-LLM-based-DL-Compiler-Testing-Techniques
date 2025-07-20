mat1 = torch.randn(2, 3)
mat2 = torch.randn(3, 2)
result = torch.Tensor.addmm(mat1, mat1, mat2)