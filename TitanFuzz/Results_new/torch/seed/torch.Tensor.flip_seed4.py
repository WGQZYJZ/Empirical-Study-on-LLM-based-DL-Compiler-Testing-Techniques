_input_tensor = torch.randn(2, 3, 4)
_output_tensor = torch.Tensor.flip(_input_tensor, dims=(2,))