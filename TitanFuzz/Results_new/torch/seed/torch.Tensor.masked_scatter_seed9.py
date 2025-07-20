input_tensor = torch.randn(2, 3)
mask = torch.tensor([[0, 1, 1], [1, 0, 0]])
tensor = torch.tensor([[1, 1, 1], [1, 1, 1]])
torch.Tensor.masked_scatter(input_tensor, mask, tensor)