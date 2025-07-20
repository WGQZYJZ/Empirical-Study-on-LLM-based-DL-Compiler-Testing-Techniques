_input_tensor = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
_input_tensor = torch.tensor(_input_tensor, dtype=torch.float32)
torch.Tensor.byte(_input_tensor, memory_format=torch.preserve_format)