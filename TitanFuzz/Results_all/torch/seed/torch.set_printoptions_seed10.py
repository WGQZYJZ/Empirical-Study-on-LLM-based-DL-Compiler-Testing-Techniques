x = torch.rand(3, 4)
torch.set_printoptions(precision=3)
torch.set_printoptions(precision=2, threshold=1)
torch.set_printoptions(precision=2, threshold=1, edgeitems=2)
torch.set_printoptions(precision=2, threshold=1, edgeitems=2, linewidth=100)
torch.set_printoptions(precision=2, threshold=1, edgeitems=2, linewidth=100, profile='full')
torch.set_printoptions(precision=2, threshold=1, edgeitems=2, linewidth=100, profile='full', sci_mode=False)