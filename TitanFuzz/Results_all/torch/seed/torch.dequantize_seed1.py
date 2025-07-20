input_data = torch.randint(low=0, high=255, size=(1, 3, 3, 3), dtype=torch.uint8)
output = torch.dequantize(input_data)