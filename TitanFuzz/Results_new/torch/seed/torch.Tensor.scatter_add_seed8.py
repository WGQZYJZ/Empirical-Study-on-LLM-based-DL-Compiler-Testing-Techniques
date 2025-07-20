input_tensor = torch.randint(0, 10, (3, 3))
index = torch.tensor([0, 2, 1])
src = torch.tensor([1, 2, 3])
result = torch.Tensor.scatter_add(input_tensor, dim=0, index=index, src=src)