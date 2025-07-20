input_tensor = torch.randn(5, 3)
torch.Tensor.clip_(input_tensor, min=(- 0.5), max=0.5)