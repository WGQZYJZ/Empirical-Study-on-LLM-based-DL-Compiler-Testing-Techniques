input_tensor = torch.arange(1, 9, dtype=torch.float32).reshape(2, 4)
output_tensor_list = torch.Tensor.tensor_split(input_tensor, 2, dim=1)