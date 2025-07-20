input = torch.rand(1, 3, 4, 4, 4)
output_size = (2, 2, 2)
input = torch.rand(1, 3, 4, 4, 4)
output = torch.nn.functional.adaptive_avg_pool3d(input, output_size)