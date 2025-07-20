x = Variable(torch.randn(10, 5))
y = Variable(torch.randn(10, 5))
torch.nn.utils.clip_grad_norm_(x, max_norm=2, norm_type=2)
torch.nn.utils.clip_grad_norm_(y, max_norm=2, norm_type=2)