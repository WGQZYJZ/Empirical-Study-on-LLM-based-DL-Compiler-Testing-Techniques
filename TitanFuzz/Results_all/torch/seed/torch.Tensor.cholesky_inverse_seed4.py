_input_tensor = torch.rand(size=(3, 3))
_output_tensor = torch.Tensor.cholesky_inverse(_input_tensor, upper=False)