input_tensor = torch.tensor([float('nan'), float('inf'), float('-inf'), 1.0, 0.0])
output_tensor = torch.Tensor.nan_to_num(input_tensor, nan=0.0, posinf=None, neginf=None)