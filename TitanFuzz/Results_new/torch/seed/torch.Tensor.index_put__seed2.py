input_tensor = torch.randn(4, 4)
indices = torch.tensor([[0, 1], [2, 3]])
values = torch.tensor([[1, 2], [3, 4]])
torch.Tensor.index_put_(input_tensor, indices, values, accumulate=False)