
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, y1, z1, w1):
        v1 = torch.mm(x1,y1) # Matrix multiplication between input1 and input2
        v2 = torch.mm(z1,w1)# Matrix multiplication between input3 and input4
        return v1 + v2

# Initializing the model
m  = Model()

 # Inputs to the model 
 x1  = torch.randn(6000, 5)
 
 y1  = torch.randn(5, 784).type_as(x1)# Create a  matrix of size 5*784
 
 z1 =torch.randn(39200, 39200) #Create a  39200 by 39200  matrix
 
 w1  = torch.randperm(39200)# Create a random vector of size 784

__output__  = m(x1, y1, z1, w1)

