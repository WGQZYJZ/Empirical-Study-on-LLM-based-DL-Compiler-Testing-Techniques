input_tensor = torch.randint(0, 255, (1, 3, 8, 8), dtype=torch.uint8)
output_tensor = torch.dequantize(input_tensor)