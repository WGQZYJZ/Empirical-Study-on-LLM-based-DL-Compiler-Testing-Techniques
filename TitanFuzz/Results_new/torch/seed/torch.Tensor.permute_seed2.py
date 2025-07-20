_input_tensor = torch.randn(2, 3, 5)
_output_tensor = torch.Tensor.permute(_input_tensor, 0, 2, 1)