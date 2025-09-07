# Initializing the model
m1 = Model()


m2 = Model()
# Inputs to the model
input_tensor, key1  = torch.randn(10,5),torch.randn(10,8)
value3 = 10

input_tensor2 ,key2= torch.randn(9,7) , torch.randn(9,6)

__output__  = m1(input_tensor, key1, value3)

 __output__2 =m2(input_tensor2, key2,value3 )


