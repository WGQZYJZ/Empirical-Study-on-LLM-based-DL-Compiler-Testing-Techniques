_input_tensor = torch.randn(2, 3, 4)
_size = (4, 4)
_output_tensor = torch.Tensor.sum_to_size(_input_tensor, *_size)