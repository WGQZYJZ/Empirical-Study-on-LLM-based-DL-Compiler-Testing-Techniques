
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.fc = torch.nn.Linear(3, 8)
 
    def forward(self, x1):
        v1 = torch.addmm(x1, x1.t(), x1) # Multiply each of the input tensors by itself and add them together
        v2 = torch.cat([v1], dim=0)  # Concatenate all results along a specified dimension
        return self.fc(v2)


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(1, 3)
