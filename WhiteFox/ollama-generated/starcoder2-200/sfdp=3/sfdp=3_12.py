
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, x2):  # Inside this forward method we will use another input variable for a model input
        v = torch.matmul(x1, x2.transpose(-2,-1)) / 8
        return v

# Initializing the model and passing an additional argument to the forward function.
m = Model()
x1 = torch.randn(32,5)
x2 = torch.randn(5,30)
