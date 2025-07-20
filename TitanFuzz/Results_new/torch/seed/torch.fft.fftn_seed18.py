input = np.random.randint(low=0, high=100, size=(2, 3, 4, 5, 6, 7))
input = torch.from_numpy(input)
out = torch.fft.fftn(input)