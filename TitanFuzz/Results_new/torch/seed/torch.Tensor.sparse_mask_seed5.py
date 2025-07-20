input_tensor = torch.randn(3, 3, 3)
mask = torch.tensor([[0, 0, 1], [1, 0, 0], [0, 1, 1]])
output_tensor = torch.Tensor.sparse_mask(input_tensor, mask)