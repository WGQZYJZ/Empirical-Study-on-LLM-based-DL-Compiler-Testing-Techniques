
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear  = torch.nn.Linear(512 * 7, 4)
 
    def forward(self, x):
        v1  = self.linear(x)
        v2  = v1 + other_tensor
        v3  = F.relu(v2)
        return v3


# Initializing the model
m  = Model()

 # Inputs to the model
x = torch.randn(64, 512 * 7)
 
# Calling the model with inputs as parameter
__output__  = m(x)

