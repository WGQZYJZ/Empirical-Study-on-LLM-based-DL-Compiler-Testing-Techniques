_input_tensor = torch.tensor([[1, 2, 3], [4, 5, 6]])
mat2 = torch.tensor([[1, 2], [3, 4], [5, 6]])
result = torch.Tensor.mm(_input_tensor, mat2)