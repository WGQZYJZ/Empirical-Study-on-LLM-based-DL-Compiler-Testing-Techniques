
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(64, 128, bias=True)
 
    def forward(self, x1): 
        v1 = self.linear(x1)
        v2 = v1 - other
        v3 = torch.relu(v2)
 
        return v3


# Initializing the model
m  = Model()
 
 
 # Inputs to the model
other  = random.rand(64, )
 
x1  = torch.randn(80975, 64)   # Replace this line with your input tensor
 
 
 
 __output__  = m(x1)
 
 
