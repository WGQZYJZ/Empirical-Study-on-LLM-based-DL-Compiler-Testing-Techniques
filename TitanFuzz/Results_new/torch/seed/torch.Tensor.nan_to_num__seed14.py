input_tensor = torch.tensor([[1.0, (- 1.0), float('nan')], [float('inf'), float('-inf'), 1.0]])
output_tensor = torch.Tensor.nan_to_num_(input_tensor, nan=0.0, posinf=None, neginf=None)