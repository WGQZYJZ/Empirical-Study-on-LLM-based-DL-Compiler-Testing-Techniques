
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):

        # Replace dropout and rand_like nodes with lowmem/randlike in the graph of the model. 
        t0 = torch.nn.functional.dropout(x1)  
        v2  = torch.rand_like(t0, dtype=torch.float32)

        return v2


# Initializing the model