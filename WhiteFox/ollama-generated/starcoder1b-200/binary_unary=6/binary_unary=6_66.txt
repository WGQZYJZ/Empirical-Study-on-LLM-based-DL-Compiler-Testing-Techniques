
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(3, 10)
 
    def forward(self, x):
        return self.linear(x) + 10

 # Initializing the model
m = Model()

# Inputs to the model
input_tensor = torch.randn(1, 3, 64, 64)
