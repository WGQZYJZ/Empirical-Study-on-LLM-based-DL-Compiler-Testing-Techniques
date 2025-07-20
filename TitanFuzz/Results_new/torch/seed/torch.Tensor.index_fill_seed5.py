input_tensor = torch.randn(2, 3)
index_fill_tensor = torch.Tensor.index_fill(input_tensor, 0, torch.tensor([0, 1]), 0)