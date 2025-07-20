input_tensor = torch.randint(0, 255, (2, 3, 3), dtype=torch.uint8)
scale = torch.tensor(0.1)
zero_point = torch.tensor(0)
output_tensor = torch.Tensor.dequantize(input_tensor, scale, zero_point)