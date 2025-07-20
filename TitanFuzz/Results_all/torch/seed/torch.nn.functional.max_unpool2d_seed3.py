input = torch.randn(1, 1, 4, 4)
indices = torch.tensor([[[[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]]])
torch.nn.functional.max_unpool2d(input, indices, kernel_size=2, stride=2, padding=0)
input = torch.randn(1, 1, 4, 4, 4)