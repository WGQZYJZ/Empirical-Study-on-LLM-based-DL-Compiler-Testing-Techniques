
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, input1, input2, inp): 
        v1 = torch.mm(input1, input2) + inp 
        return v1

 # Initializing the model 
m = Model() 

# Inputs to the model
x1 = torch.randn(50, 784)   # A 50 x 784 tensor of random floats between -1 and 1.
x2 = torch.randn(784, 693)  # A 784 x 693 tensor of random floats between -1 and 1.
inp = torch.randn(50, 784).detach()  # A 50 x 784 tensor that does not require gradient.

# Initializing the model with inputs as defined above 
