
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        v2  = self.__output__
        v10= v2 - torch.tensor([[[-0.7453], [  1.6803], [-0.0910]]])
        v4  = torch.relu(v10)
        return v4

# Initializing the model
m = Model()

 # Inputs to the model