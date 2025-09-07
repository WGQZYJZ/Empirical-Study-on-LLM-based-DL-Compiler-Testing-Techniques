
class Model(torch.nn.Module):
    def __init__(self, dim=0):
        super().__init__()
        self.cat = torch.nn.Sequential(
            torch.nn.Linear(4*32**2, 5), 
            torch.nn.Dropout(p=1), 
        )

    def forward(self, x1):
        v1  = torch.nn.functional.linear(x1, mat) # Perform linear transformation of the input tensor followed by a dropout operation.
        v2  = self.cat([v1])
        return v2


# Initializing model with dropout and fully connected layer
m = Model(dim=0)

# Inputs to the model
x1  = torch.randn(4, 32**2, 5)
__output__  = m(x1)

