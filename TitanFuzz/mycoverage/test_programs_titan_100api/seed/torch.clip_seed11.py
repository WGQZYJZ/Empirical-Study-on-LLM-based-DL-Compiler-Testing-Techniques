x = torch.randn(10, 5)
x_clipped = torch.clip(x, min=0.5, max=0.7)
x_clipped_2 = torch.clamp(x, min=0.5, max=0.7)