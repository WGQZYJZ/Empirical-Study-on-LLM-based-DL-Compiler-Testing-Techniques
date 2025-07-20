input_tensor = torch.tensor([[True, True], [False, False]], dtype=torch.bool)
other = torch.tensor([[True, False], [False, True]], dtype=torch.bool)
torch.Tensor.bitwise_or(input_tensor, other)