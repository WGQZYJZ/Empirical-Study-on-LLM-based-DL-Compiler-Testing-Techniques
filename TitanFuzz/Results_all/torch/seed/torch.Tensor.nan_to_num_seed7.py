_input_tensor = torch.tensor([[float('nan'), (- 1.0), 0.0, 1.0, float('inf')], [float('nan'), (- 1.0), 0.0, 1.0, float('inf')]])
_output_tensor = torch.Tensor.nan_to_num(_input_tensor)