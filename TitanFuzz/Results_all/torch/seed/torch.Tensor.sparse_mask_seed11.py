_input_tensor = torch.tensor([[0, 1, 2, 3], [4, 5, 6, 7], [8, 9, 10, 11]])
_mask = torch.tensor([[0, 0, 0, 1], [0, 0, 1, 1], [0, 1, 1, 1]])
result = torch.Tensor.sparse_mask(_input_tensor, _mask)