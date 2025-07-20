input_tensor = torch.randn(3, 5)
torch.nn.init.orthogonal_(input_tensor)
input_tensor = torch.randn(3, 5)
torch.nn.init.orthogonal_(input_tensor, gain=2)