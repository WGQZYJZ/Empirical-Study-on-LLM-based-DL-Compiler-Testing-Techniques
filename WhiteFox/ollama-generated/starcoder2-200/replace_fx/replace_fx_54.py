
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        v3  = torch.rand_like(x1, 8*7*5) # generate the same size tensor filled with random numbers
        t4 = torch.nn.functional.dropout(v3, p=0.2, inplace=False) 
        return t4


# Initializing the model
m = Model()

# Inputs to the model
x1  = torch.rand(8,7,5).to("cuda") # On GPU device: (8,7,5), dtype=torch.float32
