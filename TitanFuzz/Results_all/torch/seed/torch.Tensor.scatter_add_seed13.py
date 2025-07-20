_input_tensor = torch.rand(5, 5)
_dim = 0
_index = torch.tensor([2, 3, 4])
_src = torch.rand(3, 5)
output_tensor = torch.Tensor.scatter_add(_input_tensor, _dim, _index, _src)