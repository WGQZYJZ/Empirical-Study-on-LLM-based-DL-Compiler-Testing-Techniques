data = torch.randn(1, 1, 3, 3)
torch.nn.utils.clip_grad_value_(data, 0.5)