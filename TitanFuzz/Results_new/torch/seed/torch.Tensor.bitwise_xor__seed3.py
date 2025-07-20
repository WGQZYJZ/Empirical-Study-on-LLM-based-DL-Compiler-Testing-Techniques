_input_tensor = torch.tensor([[1, 0, 0], [1, 0, 1], [1, 1, 0], [1, 1, 1]])
_other = torch.tensor([[1, 0, 1], [1, 1, 0], [1, 1, 1], [0, 0, 0]])
torch.Tensor.bitwise_xor_(_input_tensor, _other)