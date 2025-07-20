input_tensor = torch.rand(3, 3)
torch.Tensor.fill_diagonal_(input_tensor, fill_value=1.0, wrap=False)