t1 = input_tensor_A.permute(...) # Permute the first input tensor
t2 = input_tensor_B.permute(...) # Permute the second input tensor
t3 = torch.matmul(t1, t2) or t3 = torch.bmm(t1, t2) # Perform matmul or batch matmul with permuted tensors
