_input_tensor = torch.rand(3, 3)
_output_tensor = torch.Tensor.nextafter(_input_tensor, torch.rand(3, 3))