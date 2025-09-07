
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(784, 10)
 
    def forward(self, x1):
        v2  = torch.sigmoid(x1 * (v3 + 0.5)) # multiply the output of the linear transformation by another constant `0.5`, and then pass it through a sigmoid function. 
        return self.linear(t3)

# Initializing the model
m  = Model()


# Inputs to the model
x1 = torch.randn(64, 784)
