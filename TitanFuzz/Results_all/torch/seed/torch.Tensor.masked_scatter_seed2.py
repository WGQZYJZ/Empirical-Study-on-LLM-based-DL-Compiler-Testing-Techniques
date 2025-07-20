input_tensor = torch.rand(3, 4)
mask = torch.tensor([[1, 1, 0, 0], [1, 0, 1, 0], [0, 0, 1, 1]])
tensor = torch.ones(3, 4)
output_tensor = torch.Tensor.masked_scatter(input_tensor, mask, tensor)