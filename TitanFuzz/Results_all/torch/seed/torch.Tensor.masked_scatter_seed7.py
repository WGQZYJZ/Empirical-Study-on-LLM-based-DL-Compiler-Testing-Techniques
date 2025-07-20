input_tensor = torch.rand(2, 3)
mask = torch.ByteTensor([[0, 1, 1], [1, 1, 0]])
tensor = torch.rand(2, 3)
torch.Tensor.masked_scatter(input_tensor, mask, tensor)