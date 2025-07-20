input_tensor = torch.randint(0, 256, (2, 2), dtype=torch.uint8, device='cpu')
output_tensor = torch.dequantize(input_tensor)