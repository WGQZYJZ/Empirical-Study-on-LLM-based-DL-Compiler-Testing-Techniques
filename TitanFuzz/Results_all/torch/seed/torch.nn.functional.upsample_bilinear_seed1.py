N = 1
C = 3
H = 3
W = 3
input_data = [[[[1, 2, 3], [4, 5, 6], [7, 8, 9]], [[1, 2, 3], [4, 5, 6], [7, 8, 9]], [[1, 2, 3], [4, 5, 6], [7, 8, 9]]]]
input = Variable(torch.Tensor(input_data))
output = torch.nn.functional.upsample_bilinear(input, scale_factor=2)