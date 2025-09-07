
class Model(torch.nn.Module):
    def __init__(self, d1 = 8):
        super().__init__()
        self.d1 = d1
 
    def forward(self, x1):
        v1 = torch.mm(x1, x1)  # Matrix multiplication of two input tensors
        v2 = [v1] * (self.d1 + 3 - 0)  # Concatenation of the result tensor along a specified dimension
        return v2


# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
