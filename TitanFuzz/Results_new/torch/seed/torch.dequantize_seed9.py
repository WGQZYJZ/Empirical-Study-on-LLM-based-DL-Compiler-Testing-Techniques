input_tensor = torch.randint(low=0, high=255, size=(2, 3), dtype=torch.uint8)
output_tensor = torch.dequantize(input_tensor)