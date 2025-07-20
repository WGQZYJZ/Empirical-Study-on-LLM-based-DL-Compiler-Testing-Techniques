x_data = Variable(torch.Tensor([[[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]]]))
y_data = torch.nn.functional.adaptive_max_pool1d(x_data, 3)