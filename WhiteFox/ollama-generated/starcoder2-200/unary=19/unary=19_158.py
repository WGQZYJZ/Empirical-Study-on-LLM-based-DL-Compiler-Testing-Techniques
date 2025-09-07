
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        v1 = torch.nn.functional.linear(x1) 
        v2 = torch.nn.functional.sigmoid(v1) # apply sigmoid function to the output of the linear transformation
        return v2

# Initializing the model
m  = Model()

 # Inputs to the model
 x1= torch.randn(3,64) 
 