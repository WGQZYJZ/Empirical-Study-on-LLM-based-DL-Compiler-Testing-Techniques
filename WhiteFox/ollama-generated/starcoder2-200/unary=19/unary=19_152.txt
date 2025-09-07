
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1): # The model's input is the same with the previous example
        return torch.sigmoid(linear(x1))
 
# Initializing the model
m = Model()

# Inputs to the model
x2  = torch.randn(30)
