
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.fc = torch.nn.Linear(8, 16)
 
    def forward(self, x1):
        v1 = torch.addmm(x1, self.weight.T, self.bias)
        v2 = torch.cat([v1], dim=0) # The input to the next layer is the result of concatenating the result along the batch axis. This pattern occurs in fully connected layers followed by a concatenation operation.
        return v2


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 8)
