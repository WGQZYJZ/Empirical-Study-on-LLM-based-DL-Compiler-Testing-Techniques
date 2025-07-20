_input_tensor = torch.tensor([180.0, (- 90.0), 360.0, (- 45.0)])
_output_tensor = torch.Tensor.deg2rad(_input_tensor)