
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
        self.linear = torch.nn.Linear(32 * 64, 10)
 
    def forward(self, x1):
        v1  = self.linear(x1)
        v2  = torch.sigmoid(v1)
        v3  = v1  * v2
        return v3


# Initializing the model
m  = Model()

# Inputs to the model
x1  = torch.randn(1, 32*64)
 
# Outputs of the model
__output__  = m(x1)

