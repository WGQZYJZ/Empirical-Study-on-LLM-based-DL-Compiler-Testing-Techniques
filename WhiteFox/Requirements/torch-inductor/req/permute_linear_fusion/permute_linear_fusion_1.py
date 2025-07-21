t1 = input_tensor.permute(...)  # t1 is a tensor with permute operation applied
t2 = torch.nn.functional.linear(t1, weight, bias)  # Apply linear transformation
