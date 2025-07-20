abs = torch.tensor([[2.0, 3.0, 4.0, 5.0], [6.0, 7.0, 8.0, 9.0]], requires_grad=True)
angle = torch.tensor([[0.1, 0.2, 0.3, 0.4], [0.5, 0.6, 0.7, 0.8]], requires_grad=True)
output = torch.polar(abs, angle)