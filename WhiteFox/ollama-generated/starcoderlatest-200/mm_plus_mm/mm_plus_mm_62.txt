
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, x2, x3, x4):
        v1 = torch.mm(x1, x2)
        v2 = torch.mm(x3, x4)
        v3 = v1 + v2
        return v3


# Initializing the model
m = Model()

# Inputs to the model
input_data = (torch.randn(1, 3), 
              torch.randn(1, 4), 
              torch.randn(1, 5), 
              torch.randn(1, 6))
