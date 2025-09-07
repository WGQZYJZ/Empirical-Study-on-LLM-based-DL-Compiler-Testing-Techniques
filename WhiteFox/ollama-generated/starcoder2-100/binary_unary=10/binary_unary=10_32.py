
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(1024, 5)
 
    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = v1 + other_tensor # other is a tensor outside of this class which has been created at some point in time.
        v3 = torch.relu(v2)
        return v3

# Initializing the model
m  = Model()

# Inputs to the model
x1 = torch.randn(1, 512) # It's a small 4D tensor, you are free to select any input shape that is not covered by other cases.
__output__  = m(x1)

