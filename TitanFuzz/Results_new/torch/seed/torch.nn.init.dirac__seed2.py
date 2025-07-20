input_data = np.random.rand(1, 3, 3, 3)
input_data = torch.tensor(input_data)
torch.nn.init.dirac_(input_data)