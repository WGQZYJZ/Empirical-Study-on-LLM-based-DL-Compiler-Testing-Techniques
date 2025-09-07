
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(10, 5)
 
    def forward(self, x1):
        v1  = self.linear(x1)
        v2  = v1 * 0.5
        v3  = (v1  * v1  * v1 ) * 0.044715
        v4  = torch.tanh(v3)
        v5  = v4 + 1 
        v6  = v2 * v5
        return v6

# Initializing the model
m  = Model()

 # Inputs to the model
x1 = torch.randn(1, 10)
 
 __output__  = m(x1)

