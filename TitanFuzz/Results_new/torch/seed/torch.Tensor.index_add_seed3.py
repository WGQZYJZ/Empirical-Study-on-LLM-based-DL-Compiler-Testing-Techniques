input_tensor = torch.randn(4, 4)
index = torch.tensor([0, 2])
src = torch.randn(2, 4)
torch.Tensor.index_add(input_tensor, dim=0, index=index, tensor=src)