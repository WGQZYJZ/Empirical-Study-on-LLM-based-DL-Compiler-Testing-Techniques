_input_tensor = torch.randn(2, 3)
mat = torch.randn(3, 3)
output = torch.Tensor.smm(_input_tensor, mat)