
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear1 = torch.nn.Linear(8, 16)
        self.linear2 = torch.nn.Linear(32, 64)

    def forward(self, x):
        v1 = self.linear1(x) # Apply linear transformation to input tensor x and store the result in output
        v2 = F.relu(v1) # Perform relu on output of the linear transformation and store the result in output2
        v3 = torch.sigmoid(self.linear2(v2))  # Apply sigmoid function on output of the relu and store the result in output3
        return v3

# Initializing the model
m = Model()

# Inputs to the model
x = torch.randn(1, 8) # Input tensor for linear transformation is x
