
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(256 * 48, 10)
 
    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = torch.sigmoid(v1)
        v3 = v1 * v2
        return v3


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(5, 49088) # Shape of input should match the input shape of the convolutions in the previous example. Here we add 49088 = (256 * 48). 

__output__  = m(x1)

