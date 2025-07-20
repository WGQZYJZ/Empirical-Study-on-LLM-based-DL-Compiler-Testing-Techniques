A = torch.tensor([[1, 2, 3], [4, 5, 6], [7, 8, 9]], dtype=torch.float)
_input_tensor = torch.tensor([[1], [2], [3]], dtype=torch.float)
output = torch.Tensor.solve(_input_tensor, A)