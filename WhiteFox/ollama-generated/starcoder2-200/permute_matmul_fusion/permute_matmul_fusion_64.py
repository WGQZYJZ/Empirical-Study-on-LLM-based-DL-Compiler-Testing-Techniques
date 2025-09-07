t1  = torch.bmm(t1_1, t1_2) or torch.matmul(t1_1, t1_2)
t2  = torch.nn.functional.linear(t3_1, ...) # Apply linear transformation to the first input tensor.
t4  = torch.bmm(input_tensor_A, input_tensor_B) or torch.matmul(input_tensor_A, input_tensor_B)
