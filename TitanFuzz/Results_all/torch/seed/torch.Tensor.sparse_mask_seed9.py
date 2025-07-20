input_tensor = torch.tensor([[[1, 2, 3], [4, 5, 6], [7, 8, 9]], [[11, 12, 13], [14, 15, 16], [17, 18, 19]]])
mask_tensor = torch.tensor([[0, 1, 0], [0, 0, 1], [1, 0, 0]])
output_tensor = torch.Tensor.sparse_mask(input_tensor, mask_tensor)