input_tensor = torch.randn(3, 3, dtype=torch.float32)
torch.Tensor.fill_diagonal_(input_tensor, fill_value=1.0, wrap=False)