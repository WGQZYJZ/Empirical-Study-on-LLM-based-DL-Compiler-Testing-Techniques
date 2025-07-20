input_data = Variable(torch.Tensor([[(- 1), (- 2), 3, 4]]))
relu6 = torch.nn.ReLU6(inplace=False)