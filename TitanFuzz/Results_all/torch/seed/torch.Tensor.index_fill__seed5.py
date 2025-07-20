input_tensor = torch.randn(3, 3)
torch.Tensor.index_fill_(input_tensor, 0, torch.tensor([0, 1]), 0)