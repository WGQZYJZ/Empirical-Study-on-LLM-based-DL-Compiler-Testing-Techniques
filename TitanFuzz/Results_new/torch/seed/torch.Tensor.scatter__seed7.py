_input_tensor = torch.randn(4, 3)
_dim = 0
_index = torch.tensor([0, 2])
_src = torch.tensor([[0, 0, 0], [1, 1, 1]])
_reduce = None
torch.Tensor.scatter_(_input_tensor, _dim, _index, _src, _reduce)