logits = torch.rand(2, 3, 4)
softmax = torch.nn.functional.gumbel_softmax(logits, tau=1, hard=False, eps=1e-10, dim=(- 1))