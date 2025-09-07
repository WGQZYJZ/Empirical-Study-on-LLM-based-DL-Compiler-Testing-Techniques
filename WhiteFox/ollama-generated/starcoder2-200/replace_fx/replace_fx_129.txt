
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        v1  = torch.nn.functional.dropout(x1) # Replace the dropout node with lowmem_dropout 
        return x1 + v1


# Initializing the model
m = Model()

# Inputs to the model
x1  = torch.randn(2,3)
