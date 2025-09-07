
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(25088, 100)
 
    def forward(self, x1):
        v1  = self.linear(x1)
        v2  = v1 * 0.5
        v3  = (v1 + ((v1 * v1 * v1) * 0.044715))
        v4  = v3 * 0.7978845608028654
        v5  = torch.tanh(v4)
        v6  = v5 + 1
        v7  = v2 * v6
 
        return v7
# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(3, 3, 80, 80)

# The shape of the inputs is (3, 3, 80, 80). We expect this shape for the PyTorch's Conv2d to work properly and output a valid value when fed into the Model

