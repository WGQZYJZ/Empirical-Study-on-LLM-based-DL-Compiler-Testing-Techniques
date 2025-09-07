
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(2, 2)

    def forward(self, x1):
        v1 = torch.nn.functional.dropout(x1, p=0.25) # Dropout a linear transformation of the input tensor 
        v2 = torch.rand_like(v1, ...)
        return v2


# Initializing the model
m = Model()
m(torch.randn(1, 2, 2))
