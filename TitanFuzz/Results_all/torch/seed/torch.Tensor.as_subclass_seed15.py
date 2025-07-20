_input_tensor = torch.rand(2, 3)
_output_tensor = torch.Tensor.as_subclass(_input_tensor, torch.FloatTensor)