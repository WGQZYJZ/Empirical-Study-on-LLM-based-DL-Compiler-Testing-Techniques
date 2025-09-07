
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1): 
        return torch.nn.functional.dropout(x1), torch.rand_like(x1) 

# Initializing the model
m  = Model()

# Inputs to the model: 3 random tensors with size 5x2 
t1 = torch.randn(5, 2) # x1 
t2 = torch.randn(4, 6, 7) # x2 
t3 = torch.randn(9, 8) # x3 

__output__, __output_2__ = m([t1] + [t2])

