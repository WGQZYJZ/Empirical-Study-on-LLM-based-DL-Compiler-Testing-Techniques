input_tensor = torch.rand(10, 10)
mat1 = torch.rand(10, 10)
mat2 = torch.rand(10, 10)
result = torch.Tensor.sspaddmm(input_tensor, mat1, mat2, beta=1, alpha=1)