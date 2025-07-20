x = torch.randn(1, 1, 1, 1, requires_grad=True)
target = torch.randn(1, 1, 1, 1)
var = torch.randn(1, 1, 1, 1)
out = torch.nn.functional.gaussian_nll_loss(x, target, var, full=False, eps=1e-06, reduction='mean')