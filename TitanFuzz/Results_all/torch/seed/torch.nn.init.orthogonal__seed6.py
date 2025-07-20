input_data = np.random.randn(2, 3)
tensor = torch.Tensor(input_data)
torch.nn.init.orthogonal_(tensor, gain=1)