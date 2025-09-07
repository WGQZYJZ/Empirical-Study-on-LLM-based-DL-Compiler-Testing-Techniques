
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, inp1=None, inp2=None):
        v1 = torch.mm(inp1, inp2) # Matrix multiplication on two input tensors
        return v1 + inp

# Initializing the model
m = Model()

