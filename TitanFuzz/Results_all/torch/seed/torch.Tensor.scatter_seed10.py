input_tensor = torch.rand(3, 5)
index = torch.tensor([[4, 5, 4, 1], [3, 3, 2, 0]])
src = torch.tensor([[1, 0, 1, 0], [1, 1, 0, 0]])
output_tensor = torch.Tensor.scatter(input_tensor, dim=0, index=index, src=src)