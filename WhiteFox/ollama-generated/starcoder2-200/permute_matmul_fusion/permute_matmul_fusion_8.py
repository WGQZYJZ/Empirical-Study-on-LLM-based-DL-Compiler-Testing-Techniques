t1 = input_tensorA.permute(...)  # Permute the input tensor A
t2 = input_tensorB.permute(...)  # Permute the input tensor B
t3 = torch.bmm(input_tensorA, t2)  # or torch.matmul(input_tensorA, t1) 
t1 = input_tensorA.permute(...)  # Permute the input tensor A
t2 = torch.bmm(input_tensorB, t1)  # or torch.matmul(input_tensorB, t2) 
