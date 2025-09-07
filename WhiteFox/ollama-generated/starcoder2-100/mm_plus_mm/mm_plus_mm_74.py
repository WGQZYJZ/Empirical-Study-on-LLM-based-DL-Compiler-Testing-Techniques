t3 = torch.mul(x0, x2) # Elementwise multiplication between two tensors x0 and x2 with same shape
t6 = torch.pow(input1, t2)  # Tensor exponentiation with two tensors input1 and t2 of the same shape 
t7  = t3 / t4 * t5 + t8  # Division, multiplication, addition and modulus operations between three tensors t3, t4, t5 in the following sequence. These three tensors are of equal shapes and same shape as each other. A tensor t6 is also of equal shape with respect to these three tensors
t10 = torch.div(input1, input2)  # Division operation between two tensors x0 and x4 that have the same shape. 
