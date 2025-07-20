input = torch.arange(1, 25, dtype=torch.float32).view(1, 1, 4, 6)
torch.nn.functional.unfold(input, kernel_size=3, stride=2, padding=1)
input = torch.arange(1, 25, dtype=torch.float32).view(1, 1, 4, 6)