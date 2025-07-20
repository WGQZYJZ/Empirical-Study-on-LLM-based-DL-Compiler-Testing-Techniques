input_tensor = torch.tensor([[0.0, 0.0, 1.0], [0.0, 1.0, 0.0], [1.0, 0.0, 0.0]])
output_tensor = torch.Tensor.nan_to_num_(input_tensor, nan=0.0, posinf=None, neginf=None)