input_tensor = torch.arange(start=1, end=13, dtype=torch.float32).reshape(3, 4)
output_tensors = torch.Tensor.tensor_split(input_tensor, 2, dim=1)