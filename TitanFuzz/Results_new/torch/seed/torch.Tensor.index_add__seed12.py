input_tensor = torch.randn(4, 3)
index = torch.tensor([0, 2])
tensor = torch.tensor([[1, 1, 1], [1, 1, 1]])
torch.Tensor.index_add_(input_tensor, dim=0, index=index, tensor=tensor)