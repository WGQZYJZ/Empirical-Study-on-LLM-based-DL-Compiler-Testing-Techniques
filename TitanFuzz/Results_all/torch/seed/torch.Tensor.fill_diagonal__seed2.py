input_tensor = torch.randint(low=0, high=10, size=(3, 3), dtype=torch.int32)
torch.Tensor.fill_diagonal_(input_tensor, fill_value=100, wrap=False)