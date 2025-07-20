input_tensor = torch.randint(0, 2, (3, 3), dtype=torch.uint8)
output_tensor = torch.Tensor.bitwise_not_(input_tensor)