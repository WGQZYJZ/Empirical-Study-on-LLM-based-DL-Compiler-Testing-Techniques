input_data = Variable(torch.Tensor([[[[1, 1, 1], [1, 1, 1], [1, 1, 1]]]]))
max_pooling_layer = torch.nn.functional.max_pool2d(input_data, kernel_size=(2, 2))