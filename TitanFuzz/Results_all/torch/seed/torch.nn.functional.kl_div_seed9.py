input = torch.tensor([[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]])
target = torch.tensor([[0.0, 0.0, 0.0], [0.0, 0.0, 0.0]])
torch.nn.functional.kl_div(input, target, size_average=None, reduce=None, reduction='mean', log_target=False)