input_tensor = torch.tensor([[1, 2, 3], [4, 5, 6]])
mask = torch.tensor([[True, False, True], [True, True, False]])
output_tensor = torch.Tensor.sparse_mask(input_tensor, mask)