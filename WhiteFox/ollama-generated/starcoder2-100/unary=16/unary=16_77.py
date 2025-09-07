
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(784, 512)

    def forward(self, x1):
        v1 = self.linear(x1) # Applying a linear transformation to the input tensor
        v2 = F.relu(v1)    # Applying the ReLU activation function to the output of the linear transformation
        return v2


# Initializing the model and inputs to the model 
m  = Model()
x1 = torch.randn(64, 784)
