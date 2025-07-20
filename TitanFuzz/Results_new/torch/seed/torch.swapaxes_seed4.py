x = torch.arange(0, 9, 1)
x = x.view(3, 3)
y = torch.swapaxes(x, 0, 1)