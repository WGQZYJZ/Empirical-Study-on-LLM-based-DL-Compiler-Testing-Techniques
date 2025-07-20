input_tensor = torch.randn(2, 3)
index = torch.tensor([0, 2], dtype=torch.long)
tensor = torch.tensor([1, 2], dtype=torch.float)
torch.Tensor.index_add_(input_tensor, dim=0, index=index, tensor=tensor)