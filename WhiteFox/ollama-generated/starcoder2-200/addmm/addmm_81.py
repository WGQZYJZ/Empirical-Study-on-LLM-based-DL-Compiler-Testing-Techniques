
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, inp1, inp2=None):
         v1 = torch.mm(inp1, inp2) # Matrix multiplication on two input tensors
         v3 = v1 + inp  # Matrix multiplication and addition
         return v3

# Initializing the model
m = Model()
x1 = torch.randn(50, 40)


