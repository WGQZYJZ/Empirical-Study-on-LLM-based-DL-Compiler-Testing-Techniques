
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(1024, 512)
 
    def forward(self, x1):
        v1  = self.linear(x1)
        v2  = v1 + other_tensor # passing a new tensor in as a keyword argument to the linear transformation
        v3  = torch.relu(v2)
__output__  = m(x1)


# Initializing the model