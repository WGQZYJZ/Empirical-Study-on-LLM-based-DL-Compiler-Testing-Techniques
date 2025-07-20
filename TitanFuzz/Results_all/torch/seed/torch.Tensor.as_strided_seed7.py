input_tensor = torch.arange(0, 8, dtype=torch.float32).reshape((2, 2, 2))
output_tensor = torch.Tensor.as_strided(input_tensor, size=(2, 2, 4), stride=(2, 2, 2))