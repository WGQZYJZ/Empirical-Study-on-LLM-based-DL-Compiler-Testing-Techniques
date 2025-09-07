
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(32 * 4 * 4, 32)
 
    def forward(self, x1):
        v1 = self.linear(x1.view(x1.size()[0], -1)) # This is a linear transformation with weight shape [32 * 4 * 4, 32] and bias shape [32]
        v2 = torch.sigmoid(v1) + other_tensor # This is adding the tensor other to the output of the sigmoid function
        return v2


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
