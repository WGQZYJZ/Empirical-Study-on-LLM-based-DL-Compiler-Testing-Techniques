_input_tensor = torch.randint(0, 10, (2, 3), dtype=torch.int32)
other = torch.randint(0, 10, (2, 3), dtype=torch.int32)
result = torch.Tensor.ne(_input_tensor, other)