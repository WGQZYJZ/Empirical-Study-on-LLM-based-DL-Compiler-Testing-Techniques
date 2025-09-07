
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, x2):
        v1 = torch.mm(x1, x2)  # Perform two matrix multiplications
        v2 = x1 + x2  # Add the results of the two matrix multiplications
        return v3


# Inputs to the model
x1 = torch.randn(10, 3)  # A tensor with shape (5, 3)
x2 = torch.randn(10, 3)  # A tensor with shape (5, 3)
