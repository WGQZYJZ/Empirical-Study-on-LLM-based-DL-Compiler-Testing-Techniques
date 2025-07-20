input_tensor = torch.randint(0, 10, (3, 3))
torch.Tensor.fill_diagonal_(input_tensor, fill_value=1, wrap=False)