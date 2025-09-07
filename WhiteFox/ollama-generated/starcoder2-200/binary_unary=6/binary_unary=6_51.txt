
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        v1 = self.linear0(x1) # Linear transformation (without bias term)
        v2 = self.linear3(v1 + 16777215) # Add a constant to the output of linear transformation and then apply the ReLU activation function
        return v2


m = Model()

# Inputs for the model
x1 = torch.randn(4, 8)
 
