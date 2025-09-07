
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1): 
        v2 = torch.relu(x1)
        return 0.5 * v2

# Initializing the model
m  = Model()

 # Inputs to the model
x1= torch.randn(4,3,64,64)
