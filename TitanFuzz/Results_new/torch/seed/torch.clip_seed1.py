input_data = torch.arange(20, dtype=torch.float32).reshape(4, 5)
result = torch.clip(input_data, min=5, max=15)