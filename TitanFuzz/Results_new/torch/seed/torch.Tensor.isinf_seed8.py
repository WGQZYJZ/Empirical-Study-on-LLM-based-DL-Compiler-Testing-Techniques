_input_tensor = torch.Tensor([float('inf'), float('-inf'), float('nan')])
_output_tensor = torch.Tensor.isinf(_input_tensor)