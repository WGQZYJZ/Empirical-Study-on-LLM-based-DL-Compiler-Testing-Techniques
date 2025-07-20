input_data = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], dtype=np.uint8)
input_tensor = torch.from_numpy(input_data)
output_tensor = torch.Tensor.dequantize(input_tensor)