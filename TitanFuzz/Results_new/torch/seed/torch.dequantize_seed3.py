tensors = torch.randint(0, 255, (3, 3), dtype=torch.uint8)
tensors = torch.dequantize(tensors)