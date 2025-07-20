tensors = torch.randint(0, 256, (3, 3), dtype=torch.uint8)
torch.dequantize(tensors)