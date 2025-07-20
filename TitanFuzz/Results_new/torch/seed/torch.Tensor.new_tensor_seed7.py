input_tensor = torch.ones(3, 3)
output_tensor = torch.Tensor.new_tensor(input_tensor, data=[1, 2, 3, 4, 5, 6, 7, 8, 9], dtype=torch.float32)