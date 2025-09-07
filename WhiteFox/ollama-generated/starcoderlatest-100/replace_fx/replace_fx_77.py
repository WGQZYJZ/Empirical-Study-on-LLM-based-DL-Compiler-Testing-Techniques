
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(2, 2)

    def forward(self, x1):
        v1 = torch.nn.functional.dropout(x1, p=0.5) # The `torch.nn.functional.dropout` function is invoked
        v2 = torch.rand_like(v1)   # The `torch.rand_like` function is invoked with the same input tensor as argument 
                                   # (i.e., x1 in this example). 
        return v2


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(1, 2, 2)
