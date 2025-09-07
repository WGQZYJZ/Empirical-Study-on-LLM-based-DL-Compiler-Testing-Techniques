
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        v1 = torch.nn.functional.dropout(x1) # Applies dropout to the input tensor 
        v2  = torch.rand_like(v1)
        return v2
# Initializing model with the graph mode
m = Model()
