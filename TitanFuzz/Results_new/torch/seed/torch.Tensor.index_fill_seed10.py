_input_tensor = torch.randn(3, 3)
_dim = 1
_index = torch.tensor([0, 2])
_value = 2.0
torch.Tensor.index_fill(_input_tensor, _dim, _index, _value)