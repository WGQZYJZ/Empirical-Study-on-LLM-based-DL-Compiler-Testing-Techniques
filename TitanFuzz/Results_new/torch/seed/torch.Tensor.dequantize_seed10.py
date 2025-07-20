input_tensor = torch.randint(0, 255, (2, 3, 3), dtype=torch.uint8)
output_tensor = torch.Tensor.dequantize(input_tensor)