
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear  = torch.nn.Linear(512, 512)
        self.activation = torch.nn.Sigmoid()
 
    def forward(self, x1):
        v1  = self.linear(x1)
        v2  = self.activation(v1)
        return v1 * v2

# Initializing the model
m  = Model()

 # Inputs to the model