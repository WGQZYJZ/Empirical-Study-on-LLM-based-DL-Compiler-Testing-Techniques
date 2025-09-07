
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        v1 = torch.nn.Linear()(x1)  # apply linear transformation to the input tensor
        v2 = torch.sigmoid(v1)  # Apply sigmoid function to the output of the linear transformation
        return v2

# Initializing model
m  = Model()
# Input for the model
x1 = torch.randn(3,5)
