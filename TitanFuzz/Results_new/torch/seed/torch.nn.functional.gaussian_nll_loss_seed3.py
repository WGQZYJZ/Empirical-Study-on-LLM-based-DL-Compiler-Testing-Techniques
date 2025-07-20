input = torch.Tensor([[1, 2, 3], [4, 5, 6]])
target = torch.Tensor([[1, 2, 3], [4, 5, 6]])
var = torch.Tensor([[1, 2, 3], [4, 5, 6]])
output = torch.nn.functional.gaussian_nll_loss(input, target, var, full=False, eps=1e-06, reduction='mean')