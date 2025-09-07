
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(64*2, 10)
 
    def forward(self, x1):
        v1 = self.linear(x1)
        return v1


# Initializing the model
m = Model()

def generate_input():
    # The generated input tensor is randomized and reshaped to be compatible with both data types and devices used by PyTorch.
    x1 = torch.randn(2, 3, 64, 64) * 500 - 250
    return x1

# Inputs to the model
x1 = generate_input()
