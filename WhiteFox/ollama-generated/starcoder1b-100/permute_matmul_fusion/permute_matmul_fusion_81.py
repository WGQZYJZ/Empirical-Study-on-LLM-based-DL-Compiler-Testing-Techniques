t1  = input_tensor_A.permute(...) # Permute the input tensor A
t2 = input_tensor_B.permute(...) # Permute the input tensor B
t3 = torch.cat((t1, t2), dim=2)  # or concat(t1, t2)
