_input_tensor = torch.randn(3, 4)
_dim = 0
_index = torch.tensor([1, 1, 2, 2])
_src = torch.tensor([1, 2, 3, 4])
_reduce = None
_output_tensor = torch.Tensor.scatter_(_input_tensor, _dim, _index, _src, _reduce)