input_data = torch.randint(1, 10, (3, 3), dtype=torch.float32)
output = torch.polygamma(1, input_data)