tensor1 = torch.tensor([[1, 2], [3, 4]])
tensor2 = torch.tensor([[5, 6], [7, 8]])
tensor3 = torch.tensor([[9, 10], [11, 12]])
torch.Tensor.addcmul_(tensor1, tensor2, tensor3)