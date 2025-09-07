
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, x2, x3):
        v1 = torch.mm(x1, x2)
        v2 = torch.mm(x3, x4)
        v3 = v1 + v2
        return v6


# Initializing the model
m = Model()

# Inputs to the model
input_tensor 0 = torch.randn(1, 8, 128, 128)
input_tensor 1 = torch.randn(4, 3, 64, 64)
input_tensor 2 = torch.randn(7, 2, 32, 32)
