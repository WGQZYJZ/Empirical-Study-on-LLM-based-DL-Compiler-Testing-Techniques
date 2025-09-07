
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        v2 = torch.relu(x1 + self.__other__) 
        return v2 
 
    @property
    def __other__(self):
        return 5

# Initializing the model<|end_of_code|>
m = Model()

 # Inputs to the model
x1 = torch.randn(4) 

 