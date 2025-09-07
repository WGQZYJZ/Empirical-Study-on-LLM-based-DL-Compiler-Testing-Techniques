
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear  = torch.nn.Linear(256, 10)
 
    def forward(self, x1):
        v1  = self.linear(x1) 
        v3  = relu(v2)
        return v3


# Initializing the model
m  = Model()

 # Inputs to the model
other  = torch.randn(64, 8)  
x1  = torch.randn(10, 64, 64, 57)
 
# The output of the model is used as an input for the next part of the analysis.
