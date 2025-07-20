input = Variable(torch.Tensor([[[[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]]]))
torch.nn.functional.lp_pool2d(input, norm_type=2, kernel_size=2, stride=2)
torch.nn.functional.lp_pool2d(input, norm_type=1, kernel_size=2, stride=2)
torch.nn.functional.lp_pool2d(input, norm_type=3, kernel_size=2, stride=2)