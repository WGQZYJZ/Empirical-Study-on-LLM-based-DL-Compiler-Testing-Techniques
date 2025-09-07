
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(784, 10)

    def forward(self, x):
        v1  = self.linear(x)
        v2 = other + v1 
        return relu(v2)


# Initializing the model
m = Model()
other = torch.randn(784).cuda() # Input to the model should be on GPU, and the other tensor is not. You can assume that there are 3 input tensors to this model.

# Inputs to the model
x1 = torch.randn(1024, 784)
