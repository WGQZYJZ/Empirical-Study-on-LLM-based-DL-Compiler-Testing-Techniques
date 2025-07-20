input_tensor = torch.tensor([[1, 2, 3], [4, 5, 6]])
vec = torch.tensor([1, 2, 3])
result = torch.Tensor.mv(input_tensor, vec)