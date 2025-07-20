input_tensor = torch.randn(3, 3)
mask = torch.tensor([[0, 1, 0], [1, 0, 1], [0, 1, 0]])
sparse_masked_tensor = torch.Tensor.sparse_mask(input_tensor, mask)