input = torch.tensor([[[[0.2, 0.8], [0.5, 0.1]]]])
indices = torch.tensor([[[[0, 0], [1, 0]]]])
kernel_size = (2, 2)
output = torch.nn.functional.max_unpool2d(input, indices, kernel_size)