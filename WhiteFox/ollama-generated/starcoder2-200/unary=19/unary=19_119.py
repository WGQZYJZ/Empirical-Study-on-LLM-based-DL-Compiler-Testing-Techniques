

# Initializing the model
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(500, 1)

    def forward(self, x):
        v1 = self.linear(x) # Applying linear transformation to input tensor

        v2 = torch.sigmoid(v1)# apply sigmoid function to the output of linear transformation

        return v2

m = Model()


# Inputs to the model
x  = torch.randn(50, 500)

# Running the forward pass through the model
