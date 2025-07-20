input_tensor = torch.randn(3, 4)
mask = torch.ByteTensor([[0, 0, 1, 0], [1, 0, 0, 1], [0, 0, 1, 0]])
value = torch.FloatTensor([0.0])
output_tensor = torch.Tensor.masked_fill(input_tensor, mask, value)