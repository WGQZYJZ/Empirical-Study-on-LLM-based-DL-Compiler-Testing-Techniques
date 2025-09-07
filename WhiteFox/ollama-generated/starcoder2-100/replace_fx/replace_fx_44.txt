
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):

        v3 = torch.rand_like(x1, 0.5) # original rand_like
        v4 = torch.nn.functional.dropout(v3, 0.78, True) 
        v2 = lowmem_dropout(v4, 0.99, True, False) # replacement rand_like
        v1 = torch.nn.functional.relu(v2 - v2 + 5) 

        return (v1, v3, v2, v4)

# Initializing the model
m = Model()


# Inputs to the model
x1  = torch.randn(10, 8, 9 )
