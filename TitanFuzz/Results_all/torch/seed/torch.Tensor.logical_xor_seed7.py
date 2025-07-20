input_tensor = torch.tensor([True, False, True, False])
other = torch.tensor([True, True, False, False])
logical_xor = torch.Tensor.logical_xor(input_tensor, other)