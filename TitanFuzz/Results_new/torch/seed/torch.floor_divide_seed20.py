x = torch.tensor([1.0, 2.0, 3.0, 4.0, 5.0, 6.0], requires_grad=True)
y = torch.tensor([2.0, 2.0, 2.0, 2.0, 2.0, 2.0], requires_grad=True)
z = torch.floor_divide(x, y)