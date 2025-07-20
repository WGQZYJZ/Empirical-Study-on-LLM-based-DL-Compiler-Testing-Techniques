input_tensor = torch.tensor([[1, 2, 3], [4, 5, 6]], dtype=torch.uint8)
output_tensor = torch.dequantize(input_tensor)