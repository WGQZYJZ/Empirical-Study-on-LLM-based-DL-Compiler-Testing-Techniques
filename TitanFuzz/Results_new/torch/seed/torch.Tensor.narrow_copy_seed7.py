_input_tensor = torch.rand(4, 4)
_output_tensor = torch.Tensor.narrow_copy(_input_tensor, 0, 1, 3)