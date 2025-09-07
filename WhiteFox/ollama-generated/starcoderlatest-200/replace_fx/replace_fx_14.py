
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(2, 2)

    def forward(self, x1):
        v1 = torch.nn.functional.dropout(x1, p=0.5) # Dropout on the input tensor
        v2 = torch.rand_like(v1)                      # Generate a tensor with the same size as v1 filled with random numbers
        return v2

# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 2, 2)
