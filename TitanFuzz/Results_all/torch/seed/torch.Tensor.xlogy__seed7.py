input_tensor = torch.randint(10, (2, 3), dtype=torch.float32)
other_tensor = torch.randint(10, (2, 3), dtype=torch.float32)
torch.Tensor.xlogy_(input_tensor, other_tensor)