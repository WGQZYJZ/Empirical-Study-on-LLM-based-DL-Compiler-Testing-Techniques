input_tensor = torch.randn(3, 3)
index = torch.tensor([0, 2])
tensor = torch.tensor([[0.0, 0.0, 0.0], [1.0, 1.0, 1.0]])
torch.Tensor.index_copy_(input_tensor, dim=0, index=index, source=tensor)