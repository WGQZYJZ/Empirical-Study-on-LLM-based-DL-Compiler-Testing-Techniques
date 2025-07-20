input_tensor = torch.randn(2, 3)
index = torch.tensor([0, 2])
tensor = torch.tensor([[1, 1, 1], [2, 2, 2]])
torch.Tensor.index_copy_(input_tensor, 0, index, tensor)