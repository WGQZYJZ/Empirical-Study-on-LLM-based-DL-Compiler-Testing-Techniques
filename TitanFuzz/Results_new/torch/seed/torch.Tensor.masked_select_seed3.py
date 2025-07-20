input_tensor = torch.tensor([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
mask = torch.tensor([[0, 1], [1, 0]])
output_tensor = torch.Tensor.masked_select(input_tensor, mask)