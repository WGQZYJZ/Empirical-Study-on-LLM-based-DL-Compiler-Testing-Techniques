input_tensor = torch.randn(3, 4)
mat1 = torch.randn(4, 5)
mat2 = torch.randn(5, 6)
torch.Tensor.addmm_(input_tensor, mat1, mat2)