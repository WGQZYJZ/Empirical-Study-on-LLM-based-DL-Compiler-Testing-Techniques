input = torch.randn(1, 1, 4, 4, 4)
input = torch.randn(1, 1, 4, 4, 4)
output = torch.nn.functional.avg_pool3d(input, kernel_size=(2, 2, 2), stride=2, padding=0)