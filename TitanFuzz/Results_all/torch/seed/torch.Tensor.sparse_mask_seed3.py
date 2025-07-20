x = torch.tensor([[1, 2, 3, 4], [5, 6, 7, 8]])
mask = torch.tensor([[True, False, True, False], [False, True, False, True]])
y = torch.Tensor.sparse_mask(x, mask)