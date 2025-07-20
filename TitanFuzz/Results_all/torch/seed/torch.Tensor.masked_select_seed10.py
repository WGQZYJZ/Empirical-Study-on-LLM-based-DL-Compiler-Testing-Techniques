input_tensor = torch.Tensor([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
mask = torch.ByteTensor([[0, 0, 1], [1, 0, 1], [0, 1, 1]])
output_tensor = torch.Tensor.masked_select(input_tensor, mask)