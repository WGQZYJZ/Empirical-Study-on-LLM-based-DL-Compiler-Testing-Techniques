
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, x2):
        v1 = torch.mm(x1, x2)  # Matrix multiplication of two input tensors
        v2 = torch.cat([v1] * len(self))
        return v2

# Initializing the model
m = Model()
