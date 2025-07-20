input_data = Variable(torch.Tensor([[1, 2, 3], [4, 5, 6]]))
input_data2 = Variable(torch.Tensor([[7, 8, 9], [10, 11, 12]]))
bilinear_layer = torch.nn.Bilinear(3, 3, 2)
output = bilinear_layer(input_data, input_data2)