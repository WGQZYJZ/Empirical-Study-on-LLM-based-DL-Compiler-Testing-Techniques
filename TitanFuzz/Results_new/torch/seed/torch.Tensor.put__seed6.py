_input_tensor = torch.randn(2, 3)
index = torch.LongTensor([[0, 1], [2, 0]])
source = torch.randn(2, 2)
torch.Tensor.put_(_input_tensor, index, source, accumulate=False)