input_tensor = torch.randn(3, 4)
torch.Tensor.index_copy_(input_tensor, dim=0, index=torch.tensor([1, 2]), tensor=torch.tensor([[1, 2, 3, 4], [5, 6, 7, 8]]))