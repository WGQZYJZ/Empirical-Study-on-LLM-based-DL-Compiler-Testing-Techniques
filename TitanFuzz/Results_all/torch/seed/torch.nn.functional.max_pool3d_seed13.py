input = Variable(torch.randn(1, 1, 5, 5, 5))
kernel_size = (1, 2, 2)
pooled_output = torch.nn.functional.max_pool3d(input, kernel_size)