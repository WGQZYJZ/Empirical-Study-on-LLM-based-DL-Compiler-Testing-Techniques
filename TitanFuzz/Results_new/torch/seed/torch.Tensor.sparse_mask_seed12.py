input_tensor = torch.Tensor([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
mask = torch.tensor([[True, False, False], [False, False, True], [True, True, True]])
output_tensor = torch.Tensor.sparse_mask(input_tensor, mask)