
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(2, 2)

    def forward(self, x1):
        v1 = torch.nn.functional.dropout(x1, p=0.5) # Dropped the input tensor to simulate random values
        v2 = torch.rand_like(x1, dtype=torch.float) # Generate a tensor with the same size as input_tensor filled with random numbers
        return torch.cat([v1, v2], dim=-1)


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 4, 2)
