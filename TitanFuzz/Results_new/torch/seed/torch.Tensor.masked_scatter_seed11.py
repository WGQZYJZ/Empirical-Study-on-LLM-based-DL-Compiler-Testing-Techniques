input_tensor = torch.rand(3, 3)
mask = torch.tensor([[True, False, False], [False, True, False], [False, False, True]])
tensor = torch.tensor([[0.1, 0.2, 0.3], [0.4, 0.5, 0.6], [0.7, 0.8, 0.9]])
torch.Tensor.masked_scatter(input_tensor, mask, tensor)