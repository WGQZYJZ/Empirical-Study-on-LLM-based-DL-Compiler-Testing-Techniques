
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(32*64*64, 10)
 
    def forward(self, x):
        v1 = self.linear(x)
        v2 = torch.sigmoid(v1) # Apply the sigmoid function to the output of the linear transformation 
        return v1 * v2
 

# Initializing the model and running inference
m  = Model()
__output__  = m(torch.randn(3, 32*64*64))

