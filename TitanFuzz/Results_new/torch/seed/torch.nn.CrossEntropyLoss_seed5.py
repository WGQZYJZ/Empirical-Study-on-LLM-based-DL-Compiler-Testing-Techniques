input_data = Variable(torch.Tensor([[1, 2, 3, 4], [5, 6, 7, 8]]))
target_data = Variable(torch.LongTensor([0, 1]))
loss = torch.nn.CrossEntropyLoss()
output = loss(input_data, target_data)