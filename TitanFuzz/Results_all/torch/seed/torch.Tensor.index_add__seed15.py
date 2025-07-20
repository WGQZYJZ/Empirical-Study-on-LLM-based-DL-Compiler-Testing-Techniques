input_tensor = torch.randn(3, 4)
index = torch.tensor([0, 2])
tensor = torch.tensor([[1, 1, 1, 1], [1, 1, 1, 1]])
output_tensor = torch.Tensor.index_add_(input_tensor, dim=0, index=index, tensor=tensor)