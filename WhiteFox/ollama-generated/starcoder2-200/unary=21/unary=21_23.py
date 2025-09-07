
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        v1 = torch.tanh(x1) # Applying tanh activation to the input tensor
        return v1


# Initializing the model
m  = Model()


# Inputs to the model