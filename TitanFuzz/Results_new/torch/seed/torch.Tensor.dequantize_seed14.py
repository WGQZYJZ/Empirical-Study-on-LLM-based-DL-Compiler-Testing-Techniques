input_tensor = torch.randint(low=0, high=255, size=(1, 3, 224, 224), dtype=torch.uint8)
output_tensor = torch.Tensor.dequantize(input_tensor)