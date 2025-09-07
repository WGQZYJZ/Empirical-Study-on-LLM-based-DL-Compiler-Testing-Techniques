
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        v3 = torch.relu(x1 - 0.)
        return v3

 # Initializing the model 
 m = Model()

 # Inputs to the model
 x1 = torch.randn(256)

 