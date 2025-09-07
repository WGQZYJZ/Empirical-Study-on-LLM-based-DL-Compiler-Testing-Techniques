
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(784, 20)
    
    def forward(self, x1):
       v1 = self.linear(x1)
       v2 = torch.tanh(v1) # Apply tanh after the linear transformation
       return v2

# Initializing the model
m = Model()

# Inputs to the model
inputs_to_model = torch.randn(64, 784)

