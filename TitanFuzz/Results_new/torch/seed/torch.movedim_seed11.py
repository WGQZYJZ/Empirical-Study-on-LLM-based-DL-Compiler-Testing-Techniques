x = torch.randn(2, 3, 4)
torch.movedim(x, 0, 1)
torch.movedim(x, 1, 0)
torch.movedim(x, 0, 2)
torch.movedim(x, 2, 0)
torch.movedim(x, 0, (- 2))
torch.movedim(x, 1, (- 1))
torch.movedim(x, 0, (- 3))
torch.movedim(x, 2, (- 1))