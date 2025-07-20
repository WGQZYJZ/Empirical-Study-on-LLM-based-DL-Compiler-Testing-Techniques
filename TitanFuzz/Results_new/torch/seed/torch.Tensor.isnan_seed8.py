_input_tensor = torch.tensor([[0, 1, float('nan'), 3], [4, float('nan'), 6, 7]])
_output_tensor = torch.Tensor.isnan(_input_tensor)