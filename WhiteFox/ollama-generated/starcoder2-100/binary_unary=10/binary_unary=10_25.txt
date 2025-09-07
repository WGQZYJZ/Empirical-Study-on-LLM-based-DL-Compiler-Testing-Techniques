
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(32768, 1)
 
    def forward(self, x1):
        v1  = self.linear(x1) # Apply linear transformation to the input tensor 
        v4 = other + v1
        v5 = F.relu(v4)
        return v5


# Initializing and testing the model
m  = Model()
inputs  = torch.rand(1, 32768)
__output__  = m(inputs).numpy()

