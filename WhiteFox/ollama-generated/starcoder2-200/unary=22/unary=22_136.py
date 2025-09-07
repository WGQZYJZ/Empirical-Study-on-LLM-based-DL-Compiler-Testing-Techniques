
class Model(torch.nn.Module):
    def __init__(self, dim1=80):
        super().__init__()
        self.linear = torch.nn.Linear(3*64**2, 15)
 
    def forward(self, x1):
        v1 = self.linear(x1.view(-1))
        v2 = torch.tanh(v1)

        return v2

# Initializing the model
m = Model()

 # Inputs to the model
x1 = torch.randn(3*64**2).view(1, 3*64**2)
