input_tensor = torch.tensor([[False, False, False], [True, False, True], [False, True, False]], dtype=torch.bool)
other = torch.tensor([[True, True, True], [False, False, True], [True, False, True]], dtype=torch.bool)
result = torch.Tensor.logical_and(input_tensor, other)