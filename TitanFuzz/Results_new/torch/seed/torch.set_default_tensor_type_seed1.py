input_data = np.array([[3, 2.5], [1, (- 1)], [(- 1), (- 1.5)], [(- 3), (- 2)]])
torch.set_default_tensor_type(torch.FloatTensor)
tensor_data = torch.from_numpy(input_data)