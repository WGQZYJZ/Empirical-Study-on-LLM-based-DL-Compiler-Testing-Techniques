input_tensor = torch.tensor([[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [11, 12, 13, 14, 15, 16, 17, 18, 19, 20], [21, 22, 23, 24, 25, 26, 27, 28, 29, 30]])
output_tensor = torch.split(input_tensor, 3, dim=1)
for i in range(len(output_tensor)):
    print('Output Tensor: ', output_tensor[i])