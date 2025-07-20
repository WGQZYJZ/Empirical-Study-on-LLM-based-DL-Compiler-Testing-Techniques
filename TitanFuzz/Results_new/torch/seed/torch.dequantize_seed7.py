input_data = torch.randint(low=0, high=255, size=(3, 3), dtype=torch.uint8)
output_data = torch.dequantize(input_data)