
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(256*4*8, 9)
 
    def forward(self, x1):
        v1 = self.linear(x1) # Applying the linear transformation to an input tensor
        v2 = torch.sigmoid(v1)# Applying the sigmoid function to the output of a linear transformation 
        return v2

# Initializing the model