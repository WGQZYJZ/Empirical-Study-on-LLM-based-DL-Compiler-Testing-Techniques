

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        v2 = 0.5 * x1 + 100 # Adding a constant to the output of the linear transformation
        return v2

# Initializing the model