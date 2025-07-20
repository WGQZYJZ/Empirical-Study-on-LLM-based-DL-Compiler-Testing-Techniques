input = Variable(torch.Tensor([[[[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]]]))
max_pool_3d = torch.nn.MaxPool3d(kernel_size=(1, 2, 2), stride=None, padding=0, dilation=1, return_indices=False, ceil_mode=False)
output = max_pool_3d(input)