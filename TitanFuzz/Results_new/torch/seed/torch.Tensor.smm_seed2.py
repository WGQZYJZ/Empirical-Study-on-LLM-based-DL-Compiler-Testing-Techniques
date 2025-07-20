_input_tensor = torch.rand((1, 1, 3, 3))
mat = torch.rand((1, 1, 3, 3))
output_tensor = torch.Tensor.smm(_input_tensor, mat)