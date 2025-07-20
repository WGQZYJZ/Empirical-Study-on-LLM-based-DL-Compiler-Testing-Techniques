input_tensor = torch.randn(3, 3)
torch.Tensor.index_copy_(input_tensor, 0, torch.tensor([1, 2, 0]), input_tensor)