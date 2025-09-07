
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(2, 2)

    def forward(self, x1):
        v1 = torch.nn.functional.dropout(x1, p=0.5) # Dropout will be replaced with the lowmem_dropout replacement
        v2 = torch.rand_like(v1) # Generate a tensor filled with random numbers
        return self.linear(v2)


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(4, 8, 8)
