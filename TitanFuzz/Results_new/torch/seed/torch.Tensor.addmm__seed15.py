input_tensor = torch.randn(2, 3)
mat1 = torch.randn(3, 4)
mat2 = torch.randn(4, 3)
output_tensor = torch.Tensor.addmm_(input_tensor, mat1, mat2)