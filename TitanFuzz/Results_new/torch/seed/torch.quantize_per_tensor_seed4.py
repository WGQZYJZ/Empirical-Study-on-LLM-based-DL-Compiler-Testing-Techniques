input = np.array([[1, 2, 3], [4, 5, 6]], dtype=np.float32)
input = torch.from_numpy(input)
input_q = torch.quantize_per_tensor(input, scale=0.5, zero_point=2, dtype=torch.quint8)