input_tensor = torch.randint(low=0, high=10, size=(4, 3), dtype=torch.float)
output_tensor = torch.Tensor.cumsum_(input_tensor, dim=1, dtype=None)