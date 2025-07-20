x = torch.randn(1, 2, 3)
y = torch.randn(1, 2, 3)
torch.nn.utils.vector_to_parameters(x, y)