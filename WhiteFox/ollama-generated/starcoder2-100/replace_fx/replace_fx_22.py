
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        v2  = torch.rand_like(x1) # Use the random_like function to fill with random numbers
        v1  = torch.nn.functional.dropout(v2, p=0.5) # Dropout the values by half. 
        return v1


# Initializing the model
m = Model()

# Inputs to the model
x1  = torch.randn(3, 4)
__output__  = m(x1)