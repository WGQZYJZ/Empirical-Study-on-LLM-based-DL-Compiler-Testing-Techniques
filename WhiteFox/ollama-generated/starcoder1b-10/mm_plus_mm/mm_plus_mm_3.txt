
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, x2):
        v1 = torch.mm(x1, x2) # Matrix multiplication between x1 and x2
        v2 = torch.addcmul(v1, x1, x2) # Addition of the results of the two matrix multiplications
        return v2


# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
x2 = torch.randn(1, 4, 32, 32)
