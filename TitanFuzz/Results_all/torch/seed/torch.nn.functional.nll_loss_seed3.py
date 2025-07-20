input = torch.Tensor([[1.0, 2.0, 3.0], [4.0, 5.0, 6.0], [7.0, 8.0, 9.0]])
target = torch.LongTensor([0, 1, 2])
loss = torch.nn.functional.nll_loss(input, target)