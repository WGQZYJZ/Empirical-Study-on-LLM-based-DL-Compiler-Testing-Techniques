input_data = torch.randn(1, 3, 224, 224)
torch.random.seed()
is_cudnn_enabled = torch.backends.cudnn.enabled