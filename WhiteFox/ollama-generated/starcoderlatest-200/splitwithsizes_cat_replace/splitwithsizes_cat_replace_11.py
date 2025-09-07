t = input_tensor # The output of this operation is used as a temporary value 
output_1 = op1(input_tensor) # An arbitrary PyTorch operation applied to the input tensor
output_2 = op2(input_tensor) # An arbitrary PyTorch operation applied to the input tensor, which is computed after 'op1' has been applied. Note that the order of operations matter in this case.
t2 = torch.cat([output_1, output_2], dim=0) # Concatenate the output of two previous operations along dimension 0
x1 = input_tensor # The output of this operation is used as a temporary value
t1 = op(x1) # An arbitrary PyTorch operation applied to the input tensor and produces an intermediate tensor, where 'op' applies some kind of transformation or filtering to 'x1'. 
t2 = op(t1) # An arbitrary PyTorch operation applied to the intermediate tensor produced in the previous step and produces another intermediate tensor. The order of operations do not matter.
output_1 = op(t2) # An arbitrary PyTorch operation applied to the intermediate tensor produced in the previous step and produces an output tensor, where 'op' applies some kind of transformation or filtering to the intermediate tensor produced in the previous step. Note that the order of operations matter here too! 
output_2 = op(x1) # An arbitrary PyTorch operation applied to the input tensor and produces another output tensor. The order of operations do not matter here either.
t3 = torch.cat([output_1, output_2], dim=0) # Concatenate the output of two previous operations along dimension 0. Note that the order of concatenation matters here as well!
