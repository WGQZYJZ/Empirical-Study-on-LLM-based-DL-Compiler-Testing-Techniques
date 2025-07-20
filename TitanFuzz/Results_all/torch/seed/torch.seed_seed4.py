input_data = torch.randn(1, 1, 32, 32)
torch.seed()
torch.backends.cudnn.deterministic = True
torch.backends.cudnn.benchmark = False
torch.backends.cudnn.enabled = False