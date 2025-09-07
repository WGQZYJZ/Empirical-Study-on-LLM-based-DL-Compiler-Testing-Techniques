
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(32 * 64 * 64, 1)
 
    def forward(self, x1):
        v1 = self.linear(x1.view(x1.shape[0], -1)) # Flatten the input tensor into a 1-dim array
        v2 = torch.sigmoid(v1) # Apply sigmoid function to flattened output of linear transformation
        return v2


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(4, 3, 64, 64)
