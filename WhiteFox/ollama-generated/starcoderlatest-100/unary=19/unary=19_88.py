
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.lin = torch.nn.Linear(3 * 64 * 64, 128)
 
    def forward(self, x1):
        v1 = self.lin(x1.view(-1)) # Flatten the input tensor and then apply linear transformation to it
        v2 = torch.sigmoid(v1) # Apply sigmoid function to output of linear transformation
        return v2


# Initializing the model
m = Model()
 
# Inputs to the model
x1 = torch.randn(3, 64 * 64, requires_grad=True)
