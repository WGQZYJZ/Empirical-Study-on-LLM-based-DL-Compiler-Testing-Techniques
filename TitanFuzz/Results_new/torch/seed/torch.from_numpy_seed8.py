np_data = np.arange(6).reshape((2, 3))
torch_data = torch.from_numpy(np_data)
torch2array = torch_data.numpy()