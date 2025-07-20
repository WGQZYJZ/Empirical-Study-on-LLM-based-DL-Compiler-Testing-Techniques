input_tensor = torch.randn(4, 4)
mat1 = torch.randn(4, 4)
mat2 = torch.randn(4, 4)
output_tensor = torch.Tensor.sspaddmm(input_tensor, mat1, mat2, beta=1, alpha=1)