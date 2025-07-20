input = torch.tensor([[1, 2, 3], [4, 5, 6]])
target = torch.tensor([[1, 2, 3], [4, 5, 6]])
loss = torch.nn.functional.kl_div(input, target, size_average=None, reduce=None, reduction='mean', log_target=False)