
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(2, 2)

    def forward(self, x1):
        v1 = torch.nn.functional.dropout(x1, self.p) # Dropout applied to the input tensor
        v2 = torch.rand_like(v1)                  # Generate a tensor with the same size as v1 filled with random numbers
        return v2


# Initializing the model and specifying the dropout probability of 0.5. This specifies that all dropout operations will be replaced by lowmem_dropout nodes.
m = Model()
gm.set_config(torch.nn.functional.dropout, {"p": 0.5})


# Inputs to the model
x1 = torch.randn(1, 2, 2)
