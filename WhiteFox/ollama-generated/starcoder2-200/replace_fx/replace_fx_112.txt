
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        v3  = torch.nn.functional.dropout(x1, 0.8) # apply dropout to input tensor
        v4  = torch.rand_like(v3, dtype=torch.float64) 
        v5  = torch.nn.functional.relu(v4 + x1) # add input and dropout result

        return (v5 + v3).sum()


# Initializing the model
m = Model()

# Inputs to the model
x1  = torch.randn(2, 2, 3)

