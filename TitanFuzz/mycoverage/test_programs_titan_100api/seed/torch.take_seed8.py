a = torch.arange(0, 16)
a = a.view(4, 4)
b = torch.take(a, torch.tensor([0, 1, 2, 3]))
b = torch.take(a, torch.tensor([0, 4, 8, 12]))
b = torch.take(a, torch.tensor([1, 5, 9, 13]))
b = torch.take(a, torch.tensor([2, 6, 10, 14]))
b = torch.take(a, torch.tensor([3, 7, 11, 15]))