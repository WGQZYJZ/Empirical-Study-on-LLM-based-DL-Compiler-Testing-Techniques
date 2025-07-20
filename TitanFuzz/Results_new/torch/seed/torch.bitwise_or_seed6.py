tensor_a = torch.tensor([[True, False], [False, True]], dtype=torch.bool)
tensor_b = torch.tensor([[True, True], [False, True]], dtype=torch.bool)
tensor_c = torch.bitwise_or(tensor_a, tensor_b)
tensor_c = torch.bitwise_or(tensor_a, tensor_b, out=tensor_a)