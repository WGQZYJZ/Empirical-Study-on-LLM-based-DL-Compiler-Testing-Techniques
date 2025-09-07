
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = v1 - other
        return v2


# Initializing the model with different 'other' tensors (equivalent to initializing a new model).
m  = Model()
m_2 = Model()

# Inputs for each of the models
x1  = torch.randn(1, 3, 64, 64) # Input tensor for model m and x1 in model m_2
__output__  = m(x1)             # Output from model m with input x1

