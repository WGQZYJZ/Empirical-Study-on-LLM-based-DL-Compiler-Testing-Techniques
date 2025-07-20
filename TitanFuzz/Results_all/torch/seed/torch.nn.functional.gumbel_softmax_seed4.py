logits = torch.rand(3, 5)
samples = torch.nn.functional.gumbel_softmax(logits, tau=1, hard=False, eps=1e-10, dim=(- 1))