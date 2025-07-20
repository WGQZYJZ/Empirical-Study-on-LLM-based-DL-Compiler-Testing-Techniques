input_tensor = np.random.rand(3, 4)
input_tensor = torch.from_numpy(input_tensor)
transposed_tensor = torch.Tensor.t_(input_tensor)