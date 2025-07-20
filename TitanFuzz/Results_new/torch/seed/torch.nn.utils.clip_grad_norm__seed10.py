input_data = torch.randn(5, 4)
torch.nn.utils.clip_grad_norm_(input_data, max_norm=2, norm_type=2)