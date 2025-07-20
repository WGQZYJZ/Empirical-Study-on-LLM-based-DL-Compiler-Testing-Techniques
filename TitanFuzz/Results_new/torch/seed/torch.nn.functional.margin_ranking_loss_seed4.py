x = torch.randn(3, requires_grad=True)
y = torch.randn(3, requires_grad=True)
z = torch.randn(3, requires_grad=True)
torch.nn.functional.margin_ranking_loss(x, y, z)