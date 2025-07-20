_input_tensor = torch.rand(2, 3, 4)
_dim = 1
_index = torch.tensor([0, 2])
_tensor = torch.rand(2, 4)
torch.Tensor.index_add_(_input_tensor, _dim, _index, _tensor)