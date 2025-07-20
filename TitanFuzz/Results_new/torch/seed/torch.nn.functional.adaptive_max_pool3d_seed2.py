input = Variable(torch.randn(1, 1, 10, 10, 10))
output_size = (2, 3, 4)
torch.nn.functional.adaptive_max_pool3d(input, output_size, return_indices=False)