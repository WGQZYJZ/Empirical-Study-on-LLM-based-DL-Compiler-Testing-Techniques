input_tensor = torch.randn(1, 1, 3, 3)
mat1 = torch.randn(1, 1, 3, 3)
mat2 = torch.randn(1, 1, 3, 3)
output_tensor = torch.Tensor.addmm_(input_tensor, mat1, mat2, beta=1, alpha=1)
input_tensor = torch.randn(1, 1, 3, 3)
mat = torch.rand