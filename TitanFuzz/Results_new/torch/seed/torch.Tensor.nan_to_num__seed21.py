_input_tensor = torch.randn(3, 4)
_input_tensor[(_input_tensor > 0.5)] = torch.tensor(float('nan'))
_input_tensor[(_input_tensor < (- 0.5))] = torch.tensor(float('inf'))
_output_tensor = torch.Tensor.nan_to_num_(_input_tensor, nan=0.0, posinf=None, neginf=None)