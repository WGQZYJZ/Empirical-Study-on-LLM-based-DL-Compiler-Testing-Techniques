input_tensor = torch.Tensor(np.array([[1, 0, 0, 1], [0, 1, 1, 0]]))
other = torch.Tensor(np.array([[1, 0, 1, 0], [0, 1, 0, 1]]))
output_tensor = torch.Tensor.bitwise_xor(input_tensor, other)