mat1 = torch.randn(4, 4)
mat2 = torch.randn(4, 4)
result = torch.Tensor.sspaddmm(mat1, mat2, mat1, beta=1, alpha=1)