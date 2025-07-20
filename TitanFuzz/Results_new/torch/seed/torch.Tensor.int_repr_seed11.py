input_tensor = torch.randint(10, (1, 5), dtype=torch.int8)
output_tensor = torch.Tensor.int_repr(input_tensor)