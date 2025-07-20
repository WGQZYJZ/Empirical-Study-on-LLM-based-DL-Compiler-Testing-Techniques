a = torch.rand(4, 4)
b = a.view(16)
c = a.view((- 1), 8)
torch.set_printoptions(precision=None, threshold=None, edgeitems=None, linewidth=None, profile=None, sci_mode=None)