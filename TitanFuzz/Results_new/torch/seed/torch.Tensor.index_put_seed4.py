_input_tensor = torch.rand(4, 4)
_indices = torch.tensor([[1, 2], [2, 3]])
_values = torch.tensor([[1, 2], [3, 4]])
torch.Tensor.index_put(_input_tensor, _indices, _values, accumulate=False)