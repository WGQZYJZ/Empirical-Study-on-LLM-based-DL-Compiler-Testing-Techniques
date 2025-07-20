x = torch.randn(10, 10, 10)
torch.nn.utils.clip_grad_norm_(x, max_norm=0.5, norm_type=2.0, error_if_nonfinite=False)