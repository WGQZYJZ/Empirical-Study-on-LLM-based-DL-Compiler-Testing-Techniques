
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
       v1  = torch.nn.functional.dropout(x1, p=0) # Apply dropout to the input tensor, where the probability of each element is set to zero
       v2 = torch.rand_like(v1) 
       return v2

# Initializing the model
m = Model()

# Inputs to the model
x1  = torch.randn(32, 50)


