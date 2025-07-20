input_tensor = torch.rand(4, 4)
mat1 = torch.rand(4, 4)
mat2 = torch.rand(4, 4)
result = torch.Tensor.sspaddmm(input_tensor, mat1, mat2)