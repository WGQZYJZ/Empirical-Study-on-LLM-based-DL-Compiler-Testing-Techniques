
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        v1  = torch.randn(2) 
        v3 = torch.stack((v1, )) # Permute input tensor
        return v3


# Initializing the model
m  = Model()


# Inputs to the model
x1 = torch.randn(10)
