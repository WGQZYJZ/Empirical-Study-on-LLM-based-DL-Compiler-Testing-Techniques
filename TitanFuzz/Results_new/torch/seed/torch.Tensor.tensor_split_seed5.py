input_tensor = torch.arange(start=0, end=12, dtype=torch.float32)
input_tensor = input_tensor.view(1, 1, 12)
output_tensor = torch.Tensor.tensor_split(input_tensor, [3, 6, 9], dim=2)