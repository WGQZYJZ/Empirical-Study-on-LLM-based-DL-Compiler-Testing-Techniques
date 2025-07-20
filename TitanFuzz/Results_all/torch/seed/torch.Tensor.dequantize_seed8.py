input_tensor = torch.randint(low=0, high=255, size=(1, 3, 3, 3), dtype=torch.uint8)
dequantized_tensor = torch.Tensor.dequantize(input_tensor)