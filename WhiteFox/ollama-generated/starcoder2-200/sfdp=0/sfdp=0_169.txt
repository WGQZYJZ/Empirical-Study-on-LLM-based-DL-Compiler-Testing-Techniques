
# Initializing the model
m = MyModel(32)

 # Inputs to the model
input1 = torch.randn(30, 4096, 768)
input2 = torch.randn(30, 768, 512)
 
output = m(input1, input2)


