_input_tensor = torch.randn(4, 4)
mat = torch.randn(4, 4)
_output_tensor = torch.Tensor.smm(_input_tensor, mat)