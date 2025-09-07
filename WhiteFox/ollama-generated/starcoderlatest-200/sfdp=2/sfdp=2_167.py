
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(512, 512)
 
    def forward(self, x1, x2):
        v1 = x1 * x2
        v2 = self.linear(v1).mean([1, 2]) # Apply mean pooling on the output of the linear layer to compute a global vector for each example
        return v2


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(4, 512)
x2 = torch.randn(4, 512)
