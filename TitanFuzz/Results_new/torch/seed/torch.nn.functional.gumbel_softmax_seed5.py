logits = torch.randn(1, 5)
gumbel_softmax = torch.nn.functional.gumbel_softmax(logits, tau=1, hard=False, eps=1e-10, dim=(- 1))