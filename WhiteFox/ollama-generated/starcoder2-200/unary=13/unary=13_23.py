
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(3072, 1)
 
    def forward(self, x):
        v1  = self.linear(x)
        v2  = torch.sigmoid(v1) 
        return (v1 * v2).sum()

 # Initializing the model
m  = Model() 

 # Inputs to the model
inputs  = torch.rand(3072,) + 1
__output__  = m(inputs)

