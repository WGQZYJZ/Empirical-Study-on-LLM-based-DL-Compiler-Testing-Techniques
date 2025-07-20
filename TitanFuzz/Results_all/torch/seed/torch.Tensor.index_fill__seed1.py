input_tensor = torch.randn(2, 3)
torch.Tensor.index_fill_(input_tensor, 1, torch.tensor([0, 2]), 0)