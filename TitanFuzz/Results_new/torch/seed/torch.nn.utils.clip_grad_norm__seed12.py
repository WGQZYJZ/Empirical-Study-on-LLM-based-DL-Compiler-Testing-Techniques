x = torch.randn(1, 3, requires_grad=True)
torch.nn.utils.clip_grad_norm_(x, max_norm=2, norm_type=2, error_if_nonfinite=True)