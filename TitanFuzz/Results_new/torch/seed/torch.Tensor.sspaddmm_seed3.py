input_tensor = torch.randn(2, 3, 4, 5)
mat1 = torch.randn(4, 5)
mat2 = torch.randn(3, 4)
output_tensor = torch.Tensor.sspaddmm(input_tensor, mat1, mat2, beta=1, alpha=1)