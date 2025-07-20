a = torch.arange(0, 12)
a = a.view(3, 4)
b = torch.transpose(a, 0, 1)