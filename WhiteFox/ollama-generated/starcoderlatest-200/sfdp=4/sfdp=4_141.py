
 # Initializing the model
m = Model()

 # Inputs to the model
qk  = torch.randn(2, 4, 64, 64)
v6 ,atten_weight = m(qk)

 
