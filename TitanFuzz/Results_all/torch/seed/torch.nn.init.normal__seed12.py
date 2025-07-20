input_data = torch.randn(1, 3, 224, 224)
torch.nn.init.normal_(input_data, mean=0.0, std=1.0)