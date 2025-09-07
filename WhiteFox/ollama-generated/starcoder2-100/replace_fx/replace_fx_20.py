
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
         v1 = torch.nn.functional.dropout(x1) # replace this call with torch.nn.functional.lowmem_dropout
         return v2


# Initializing the model
m  = Model()

# Inputs to the model
x1 = torch.rand([3, 4])
