t = torch.ones(5,4)
p = torch.nn.Parameter(t) # This will convert the torch tensor to Parameter. Parameters are used for parameters in neural networks which will be optimized during training and updated accordingly.
u = t * p  # Pointwise multiplication of parameter and tensor is performed here where u is obtained as 5x4.
u = torch.transpose(u,1,2)
v = torch.nn.functional.softmax(u, dim=0)

t = torch.ones(5,4)
p = t * p # Pointwise multiplication of parameter and tensor is performed here where u is obtained as 5x4.
u = torch.transpose(u,1,2)
v = torch.nn.functional.softmax(u, dim=0)


t = torch.ones(5,7,8).permute([2, 1]) # permute is used to swap the dimensions in a tensor while keeping all the elements intact which can be done with transpose as well however, for this scenario permute is more efficient than transpose because its implementation avoids unnecessary operations.
p = t * p # Pointwise multiplication of parameter and tensor is performed here where u is obtained as 5x7 x8 .
v = torch.nn.functional.linear(u)


u  = t * p # Pointwise multiplication of parameter and tensor is performed here where u is obtained as 5x7 x8 .
v = torch.nn.functional.linear(u)


u  = t * p # Pointwise multiplication of parameter and tensor is performed here where u is obtained as 5x7 x8 .
v = torch.nn.functional.linear(u)


