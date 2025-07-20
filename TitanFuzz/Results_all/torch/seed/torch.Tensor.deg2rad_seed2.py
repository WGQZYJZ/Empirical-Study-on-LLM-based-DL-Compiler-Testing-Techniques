_input_tensor = torch.randint(0, 180, (3, 3))
_output_tensor = torch.Tensor.deg2rad(_input_tensor)