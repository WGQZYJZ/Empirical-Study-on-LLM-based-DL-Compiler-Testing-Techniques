input_tensor = torch.randn(3, 3)
mask = torch.tensor([[False, False, True], [True, False, False], [False, True, False]])
value = torch.tensor([[0.0, 0.0, 1.0], [1.0, 0.0, 0.0], [0.0, 1.0, 0.0]])
out_tensor = torch.Tensor.masked_fill(input_tensor, mask, value)