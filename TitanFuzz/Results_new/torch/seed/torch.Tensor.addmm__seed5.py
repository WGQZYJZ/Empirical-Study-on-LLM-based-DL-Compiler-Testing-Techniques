input_tensor = torch.randn(3, 2)
mat1 = torch.randn(2, 3)
mat2 = torch.randn(3, 2)
torch.Tensor.addmm_(input_tensor, mat1, mat2)