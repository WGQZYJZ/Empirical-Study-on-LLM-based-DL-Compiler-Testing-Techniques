_input_tensor = torch.randn(2, 3)
output_tensor = torch.Tensor.map_(_input_tensor, torch.abs)