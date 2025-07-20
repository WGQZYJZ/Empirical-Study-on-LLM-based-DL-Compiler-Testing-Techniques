_input_tensor = torch.randn(1, 2, 3, 4)
_output_tensor = torch.Tensor.as_subclass(_input_tensor, torch.FloatTensor)