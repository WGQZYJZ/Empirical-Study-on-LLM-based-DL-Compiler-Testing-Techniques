data = [[1, 2, 3], [4, 5, 6]]
_input_tensor = torch.Tensor(data)
output_tensor = torch.Tensor.sparse_dim(_input_tensor)