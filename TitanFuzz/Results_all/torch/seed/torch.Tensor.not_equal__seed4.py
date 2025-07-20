input_tensor1 = torch.tensor([[0, 0, 0], [0, 0, 0], [0, 0, 0]])
input_tensor2 = torch.tensor([[0, 0, 0], [0, 0, 0], [0, 0, 0]])
output_tensor = torch.Tensor.not_equal_(input_tensor1, input_tensor2)