input_tensor = torch.rand(3, 4)
mask = torch.ByteTensor([[0, 0, 0, 0], [1, 1, 1, 1], [1, 0, 1, 0]])
output_tensor = torch.Tensor.masked_select(input_tensor, mask)