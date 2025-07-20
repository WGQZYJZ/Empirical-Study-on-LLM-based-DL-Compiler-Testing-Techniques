_input_tensor = torch.rand(3, 4)
_dim = 1
_index = torch.tensor([0, 2, 3])
_tensor2 = torch.rand(3, 4)
torch.Tensor.index_copy(_input_tensor, _dim, _index, _tensor2)