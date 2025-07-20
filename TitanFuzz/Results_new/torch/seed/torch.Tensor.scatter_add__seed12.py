input_tensor = torch.randn(3, 4)
index_tensor = torch.tensor([[0, 1, 2, 0], [1, 0, 1, 3]])
src_tensor = torch.tensor([[1, 2, 3, 4], [5, 6, 7, 8]])
torch.Tensor.scatter_add_(input_tensor, dim=0, index=index_tensor, src=src_tensor)