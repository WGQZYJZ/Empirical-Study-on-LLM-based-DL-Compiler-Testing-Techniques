input_tensor = torch.randn(2, 3)
index = torch.tensor([0, 2])
tensor = torch.tensor([0.1, 0.2])
torch.Tensor.index_add_(input_tensor, dim=1, index=index, tensor=tensor)