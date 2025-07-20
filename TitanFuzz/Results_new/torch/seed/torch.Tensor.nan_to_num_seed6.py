input_tensor = torch.tensor([[1, 2, 3, 4], [float('nan'), float('inf'), float('-inf'), float('inf')]])
output_tensor = torch.Tensor.nan_to_num(input_tensor, nan=0.0, posinf=None, neginf=None)