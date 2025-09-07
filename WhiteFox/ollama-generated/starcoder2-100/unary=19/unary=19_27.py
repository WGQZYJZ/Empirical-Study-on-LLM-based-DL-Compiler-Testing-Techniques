
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        v1 = torch.nn.Linear()(x1)  # Apply linear transformation to the input tensor 
        v2 = torch.sigmoid(v1)  # Apply sigmoid function to the output of linear transformation
        return v2

# Initializing the model
m  = Model()
 
# Inputs to the model
x1 = torch.randn(1,3072).type(torch.float32)
