input_tensor = torch.randn(3, 3)
index = torch.tensor([0, 2])
tensor = torch.tensor([1, 2])
output = torch.Tensor.index_add_(input_tensor, dim=0, index=index, tensor=tensor)