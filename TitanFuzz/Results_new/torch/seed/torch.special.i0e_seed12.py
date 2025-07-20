x = np.linspace((- 1), 1, num=100)
x = torch.from_numpy(x)
y = torch.special.i0e(x)