input_tensor = torch.randn(3, 3)
torch.Tensor.fill_diagonal_(input_tensor, fill_value=0.5, wrap=False)