

# Initializing the model
m  = Model()
# Inputs to the model
input1, input2 = torch.randn(4, 5), torch.randn(4, 8)
# Generating outputs for this model:
output0, output1 = m(input1, input2)

