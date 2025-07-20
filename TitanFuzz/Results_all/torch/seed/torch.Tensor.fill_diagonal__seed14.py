input_tensor = torch.randn(4, 4)
torch.Tensor.fill_diagonal_(input_tensor, 1, wrap=False)