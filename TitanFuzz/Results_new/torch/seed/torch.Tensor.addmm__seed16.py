input_tensor = torch.randn(10, 20)
mat1 = torch.randn(20, 30)
mat2 = torch.randn(30, 40)
output_tensor = torch.Tensor.addmm_(input_tensor, mat1, mat2, beta=0.5, alpha=0.5)