x = torch.randn(1, 3, 5, 5)
torch.nn.functional.instance_norm(x)
torch.nn.functional.instance_norm(x, running_mean=None, running_var=None, weight=None, bias=None, use_input_stats=True, momentum=0.1, eps=1e-05)