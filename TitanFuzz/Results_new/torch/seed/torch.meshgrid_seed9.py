x = torch.tensor([(- 1.0), 0.0, 1.0, 2.0, 3.0, 4.0])
y = torch.tensor([5.0, 6.0, 7.0, 8.0, 9.0, 10.0])
(grid_x, grid_y) = torch.meshgrid(x, y)