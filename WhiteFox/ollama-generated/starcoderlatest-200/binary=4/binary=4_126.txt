
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(64*3*3, 256)
 
    def forward(self, x1):
        v1 = self.linear(x1.view(-1, -1))
        return v1


# Initializing the model
m = Model()

# Inputs to the model
input_tensor = torch.randn(10, 3, 64, 64)
other_tensor = torch.ones(5, 256)
