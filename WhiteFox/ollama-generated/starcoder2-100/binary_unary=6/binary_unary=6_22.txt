
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(1024, 576)
 
    def forward(self, x):
        v1  = self.linear(x)
        v3  = torch.max(v1-other, min_value) 
        return relu(v3)


# Initializing the model
m  = Model()

# Inputs to the model
x  = torch.randn(2048*576).reshape((1, 2048))

__output__  = m(x)