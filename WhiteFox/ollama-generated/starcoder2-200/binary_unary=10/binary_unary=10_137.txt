
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(32768, 10)
 
    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = v1 + other # Any tensor of the same size can be added here because the model does not define this variable beforehand and cannot be passed as a parameter to the model.
        v3 = torch.nn.functional.relu(v2)
        return v3


# Initializing the model
m  = Model()

 # Inputs to the model
x1  = torch.randn(50, 32768)
 
 