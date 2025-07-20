input_tensor = torch.tensor([[0, 0], [0, 1], [1, 0], [1, 1]])
output_tensor = torch.Tensor.logical_xor(input_tensor, other=input_tensor)