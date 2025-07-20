input_tensor = torch.tensor([[1.0, 2.0, 3.0], [4.0, 5.0, 6.0], [7.0, 8.0, 9.0]])
output_tensor = torch.Tensor.nan_to_num_(input_tensor, nan=0.0, posinf=None, neginf=None)