input_tensor = torch.ones(size=(1, 5))
mat2 = torch.randn(size=(5, 3))
output = torch.Tensor.mm(input_tensor, mat2)