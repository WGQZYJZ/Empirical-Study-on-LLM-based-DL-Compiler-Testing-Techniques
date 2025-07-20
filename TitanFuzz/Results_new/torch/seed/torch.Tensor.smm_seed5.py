input_tensor = torch.randn(2, 3)
mat = torch.randn(3, 4)
output_tensor = torch.Tensor.smm(input_tensor, mat)