
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(28 * 14, 7)
    
    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = (v1 > 0).type_as(torch.tensor([0]))
        v3 = -v2 * torch.sigmoid(-v1) 
        return torch.where(v2, v1, v3), v2

# Initializing the model
m  = Model()

# Inputs to the model
x1 = torch.randn(14, 784) # This is an input tensor for the Leaky ReLU model with 784 elements in each row and 14 rows

__output__, __bool_tensor__ = m(x1)
