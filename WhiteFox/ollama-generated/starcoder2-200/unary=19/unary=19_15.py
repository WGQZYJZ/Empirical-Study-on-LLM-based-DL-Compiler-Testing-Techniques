
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(784, 2)
 
    def forward(self, x1):
        v0 = (x1.view(-1, 784)) 
        v1 = self.linear(v0)
        v3 = torch.sigmoid(v1) # The sigmoid function is not in the public API set provided by PyTorch
        return v3

# Initializing the model
m  = Model()

# Inputs to the model
