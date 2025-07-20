x = torch.tensor([1, 2, 3, 4, 5])
y = torch.tensor([10, 20, 30, 40, 50])
z = torch.tensor([100, 200, 300, 400, 500])
torch.cartesian_prod(x, y, z)