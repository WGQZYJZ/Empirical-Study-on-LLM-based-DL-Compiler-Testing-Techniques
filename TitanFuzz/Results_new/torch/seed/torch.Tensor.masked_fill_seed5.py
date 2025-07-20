input_tensor = torch.randn(2, 3, dtype=torch.float)
mask = torch.ByteTensor([[0, 0, 1], [0, 1, 0]])
value = (- 1)
output_tensor = torch.Tensor.masked_fill(input_tensor, mask, value)