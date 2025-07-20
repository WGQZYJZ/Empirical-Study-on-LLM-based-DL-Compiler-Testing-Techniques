input_data = Variable(torch.Tensor([[[[0, 1, 1.5], [2, 2.5, 3], [3.5, 4, 4.5]]]]))
output = torch.nn.functional.max_pool2d(input_data, kernel_size=2, stride=1, padding=0)