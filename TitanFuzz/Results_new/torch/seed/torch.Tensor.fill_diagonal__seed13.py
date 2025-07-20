input_tensor = torch.randn(3, 3)
fill_value = 1
torch.Tensor.fill_diagonal_(input_tensor, fill_value, wrap=False)