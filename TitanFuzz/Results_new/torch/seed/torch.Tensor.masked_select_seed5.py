input_tensor = torch.randn(3, 4)
mask = torch.ByteTensor([[0, 0, 1, 0], [1, 1, 0, 0], [0, 0, 0, 1]])
output_tensor = torch.Tensor.masked_select(input_tensor, mask)