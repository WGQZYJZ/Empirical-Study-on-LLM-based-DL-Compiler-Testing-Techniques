x = torch.tensor([[1, 2, 3], [4, 5, 6]])
y = torch.nn.functional.pad(x, (1, 1, 1, 1), mode='constant', value=0)