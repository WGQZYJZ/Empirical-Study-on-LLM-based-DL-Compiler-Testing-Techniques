
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear  = torch.nn.Linear(8, 1)
 
    def forward(self, x2):
        v7  = self.linear(x2)
        v3  = v7 + (v7 * v7  * v7 )  *  0.044715
        v9  = torch.tanh(v3) 
        v8  = v9 +  1        
        v6  = v8 * v7 
        return v6

# Initializing the model
m2  = Model()

 # Inputs to the model
x2  = torch.randn(1, 8)
__output___  = m2(x2)
