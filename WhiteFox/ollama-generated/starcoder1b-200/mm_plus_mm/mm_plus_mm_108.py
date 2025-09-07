
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, x2):
        return torch.mm(x1, x2) + 3 # Addition of the results of the two matrix multiplications

    def backward(self, dout):
        dout  = -dout  # In-place calculation for backpropagation
