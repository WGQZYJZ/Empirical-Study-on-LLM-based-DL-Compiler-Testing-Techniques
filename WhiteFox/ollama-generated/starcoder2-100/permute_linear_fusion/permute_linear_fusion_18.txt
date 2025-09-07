
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(2, 2)

    def forward(self, x1):
        v3  = x1.permute(0, 2, 1) #Perturbe the input tensor here. 
        v4  = torch.nn.functional.linear(v3, self.linear.weight, self.linear.bias)
        return v4


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(20, 256, 78) # Input to the model should be different from last time.
__output__  = m(x1)