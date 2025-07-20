_input_tensor = torch.randint(0, 2, (3, 3), dtype=torch.bool)
_output_tensor = torch.Tensor.logical_not(_input_tensor)