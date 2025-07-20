x = torch.ones(2, 2, requires_grad=True)
torch.nn.utils.clip_grad_value_(x, 0.5)