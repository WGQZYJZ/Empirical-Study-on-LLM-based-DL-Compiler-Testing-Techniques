_input_data = np.random.rand(3, 3)
_input_tensor = torch.from_numpy(_input_data)
torch.Tensor.share_memory_(_input_tensor)