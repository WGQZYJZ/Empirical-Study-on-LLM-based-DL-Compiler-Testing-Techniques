input_data = np.random.rand(3, 3).astype(np.float32)
input_tensor = torch.from_numpy(input_data)
output = torch.Tensor.is_meta(input_tensor)