input_tensor = torch.randn(3, 3)
index = torch.tensor([[0, 1, 2], [1, 2, 0]])
src = torch.tensor([[1, 2, 3], [4, 5, 6]])
output = torch.Tensor.scatter(input_tensor, dim=0, index=index, src=src)