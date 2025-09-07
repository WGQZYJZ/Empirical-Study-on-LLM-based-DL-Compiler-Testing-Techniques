
class Model(torch.nn.Module):
    def __init__(self, input1, input2):
        super().__init__()

    def forward(self, x1): # Input tensor for this model
        t  = torch.cat([input1], dim=...) 
        return torch.relu(t)

# Initializing the model
m = Model()


# Inputs to the model
input1  = torch.randn(2, 3)
input2  = torch.randn(2, 3)

__output__  = m(x1=input1, x2=input2)


