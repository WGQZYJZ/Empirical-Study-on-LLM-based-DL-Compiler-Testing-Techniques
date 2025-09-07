
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1): # Inputs are not used
        t2  = torch.tensor([0]) + self.__other__
        v4 = torch.relu(t2)
        return v4

# Initializing the model
m  = Model()

