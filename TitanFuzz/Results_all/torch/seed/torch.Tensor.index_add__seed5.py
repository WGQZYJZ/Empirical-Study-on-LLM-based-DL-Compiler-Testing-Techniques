input_tensor = torch.ones(3, 4)
index = torch.tensor([0, 2])
tensor = torch.tensor([[2, 2, 2, 2], [3, 3, 3, 3]])
torch.Tensor.index_add_(input_tensor, dim=0, index=index, tensor=tensor)