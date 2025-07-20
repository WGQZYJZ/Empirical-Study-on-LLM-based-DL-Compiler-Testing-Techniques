x = torch.randn(4, 4)
y = torch.arctanh(x)
y_np = np.arctanh(x.numpy())