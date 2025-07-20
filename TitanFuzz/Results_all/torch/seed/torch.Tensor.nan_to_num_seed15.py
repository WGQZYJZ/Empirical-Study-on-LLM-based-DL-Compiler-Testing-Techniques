input_tensor = torch.randn(1, 3)
output_tensor = torch.Tensor.nan_to_num(input_tensor, nan=0.0, posinf=None, neginf=None)