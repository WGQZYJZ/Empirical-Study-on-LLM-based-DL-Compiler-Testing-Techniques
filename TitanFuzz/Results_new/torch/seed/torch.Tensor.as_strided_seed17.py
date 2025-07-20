_input_tensor = torch.rand(4, 4)
_output_tensor = torch.Tensor.as_strided(_input_tensor, (2, 2), (2, 2))