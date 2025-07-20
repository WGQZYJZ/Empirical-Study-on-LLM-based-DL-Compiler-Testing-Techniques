_input_tensor = torch.tensor([[1, 2, 3], [float('nan'), float('inf'), float('-inf')]])
_output_tensor = torch.Tensor.nan_to_num(_input_tensor, nan=0.0, posinf=None, neginf=None)