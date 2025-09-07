
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, x2, x3, x4):
        v1  = torch.mm(x1, x2) # Matrix multiplication between input1 and input2
        v2  = torch.mm(x3, x4) # Matrix multiplication between input3 and input4
        v3  = v1 + v2 # Addition of the results of the two matrix multiplications
        return v3

# Initializing model
m  = Model()

 # Inputs to the model 
 __inputs__ = [torch.randn(5, 7), torch.randn(7, 6), torch.randn(5, 8), torch.randn(7, 9)]
 
# Predicting the output of our model using the above inputs  
__output__= m(*__inputs__)