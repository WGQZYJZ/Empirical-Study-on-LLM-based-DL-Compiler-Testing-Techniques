input_tensor = torch.randn(4, 4)
torch.Tensor.index_fill_(input_tensor, 1, torch.tensor([0, 2]), 2.0)