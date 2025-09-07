
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear1 = torch.nn.Linear(28 * 28, 30)
        self.linear2 = torch.nn.Linear(30, 256)

    def forward(self, x):
        v1  = self.linear1(x.view(-1, 28*28)) # Apply a linear transformation to the input tensor
        v2  = v1 + other  # Add another tensor to the output of the linear transformation
        return torch.relu_(v2)


# Initializing the model
m = Model()
other = torch.randn(1,30)  # Specify "other" as a random input for this model

# Inputs to the model
x1  = torch.randn(1, 28*28)
