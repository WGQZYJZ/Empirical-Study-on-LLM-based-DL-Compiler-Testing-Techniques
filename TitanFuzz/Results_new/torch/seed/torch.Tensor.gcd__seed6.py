input_tensor = torch.randint(low=1, high=10, size=(4, 4), dtype=torch.int32)
other = torch.randint(low=1, high=10, size=(4, 4), dtype=torch.int32)
torch.Tensor.gcd_(input_tensor, other)