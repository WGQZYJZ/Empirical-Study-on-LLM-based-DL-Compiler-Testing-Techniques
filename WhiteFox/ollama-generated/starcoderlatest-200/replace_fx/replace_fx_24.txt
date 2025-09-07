
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(2, 2)

    def forward(self, x1):
        v1 = torch.nn.functional.dropout(x1, p=0.5) # This is replaced with a node of type lowmem_dropout and the dropout function is deleted from the graph
        v2 = torch.rand_like(x1) # This is replaced with a node of type rand_like
        return v2

# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 2, 2)
