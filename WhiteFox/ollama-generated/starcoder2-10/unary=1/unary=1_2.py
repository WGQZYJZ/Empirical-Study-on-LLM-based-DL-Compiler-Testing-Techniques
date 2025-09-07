
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear  = torch.nn.Linear(24, 8)
 
    def forward(self, x1):
        v1  = self.linear(x1) 
        v2  = v1  * 0.5 
        v3  = (v1 ** 3 )   +   ((v1 * v1  -  1)  *   0.4789604843273372  )  
        v4  = v3  *   0.7978845608028654 
        v5  = torch.tanh(v4  +  1)
        return (v2 * v5)


# Initializing the model
m  = Model()

# Inputs to the model
x1  = torch.randn(3, 7)

__output__  = m(x1)