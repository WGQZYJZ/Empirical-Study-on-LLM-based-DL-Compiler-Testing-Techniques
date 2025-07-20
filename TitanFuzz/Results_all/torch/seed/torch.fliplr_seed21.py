x = torch.arange(12).view(3, 4).float()
y = torch.fliplr(x)
x_numpy = np.arange(12).reshape(3, 4)
y_numpy = np.fliplr(x_numpy)