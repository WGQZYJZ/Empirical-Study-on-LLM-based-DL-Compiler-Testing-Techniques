input_tensor = torch.randint(0, 10, (3, 3), dtype=torch.float32)
output_tensor = torch.Tensor.ne(input_tensor, 2)