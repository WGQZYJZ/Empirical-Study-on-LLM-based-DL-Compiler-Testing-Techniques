_input_tensor = torch.randn(3, 4, 5)
_output_tensor = torch.Tensor.moveaxis(_input_tensor, 0, 2)