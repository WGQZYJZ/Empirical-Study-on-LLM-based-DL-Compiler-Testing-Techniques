
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
        self.linear = torch.nn.Linear(512, 3000)
 
    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = v1 - other
        v3 = torch.relu(v2)

        return v3


# Initializing the model
m  = Model()
 
# Inputs to the model
x1 = torch.randn(7, 512)

 # Generating the output of the model by applying the forward function with a randomly generated input tensor
