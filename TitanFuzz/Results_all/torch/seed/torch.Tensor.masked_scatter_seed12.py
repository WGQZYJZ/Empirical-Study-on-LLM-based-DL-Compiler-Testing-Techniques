input_tensor = torch.tensor([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
mask = torch.tensor([[1, 1, 1], [0, 0, 0], [1, 1, 1]])
tensor = torch.tensor([[0, 0, 0], [1, 1, 1], [0, 0, 0]])
torch.Tensor.masked_scatter(input_tensor, mask, tensor)