
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear  = torch.nn.Linear(32*64, 8)
        self.relu1  = torch.nn.ReLU()
 
    def forward(self, x1):
        v1  = self.linear(x1)
        v2  = self.relu1(v1)
        return v2


# Initializing the model
m  = Model()

# Inputs to the model
input_tensor  = torch.randn(32, 64)
 
# Generating the inputs with a random number
v  = m(input_tensor)
 
