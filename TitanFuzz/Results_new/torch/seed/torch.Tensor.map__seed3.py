input_tensor_1 = torch.randint(0, 10, (4, 4))
input_tensor_2 = torch.randint(0, 10, (4, 4))
torch.Tensor.map_(input_tensor_1, input_tensor_2, (lambda x, y: (x + y)))