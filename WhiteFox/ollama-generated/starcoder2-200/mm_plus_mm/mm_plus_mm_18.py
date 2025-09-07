
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, x2, x3, x4):
        v1 = torch.mm(x1, x2)
        v2 = torch.mm(x3, x4) 
        v3 = v1 + v2 
        return v3 


# Initializing the model 
m = Model()


# Inputs to the model 
x1 = torch.randn(10, 5) # Input for matrix multiplication #1
x2 = torch.randn(5, 7)  # Input for matrix multiplication #2
x3 = torch.randn(6, 8) # Input for matrix multiplication #3
x4 = torch.randn(8, 9) # Input for matrix multiplication #4


# Initializing the model 

# Inputs to the model 


