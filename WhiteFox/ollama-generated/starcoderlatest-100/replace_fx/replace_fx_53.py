
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(2, 2)

    def forward(self, x1):
        v1 = torch.nn.functional.dropout(x1, p=0.5, inplace=False) # Apply dropout to the input tensor
        v2 = torch.rand_like(v1, dtype=torch.int32, device=v1.device, requires_grad=True)  # Generate a tensor with the same size as v1 filled with random numbers (type and shape should match those of the v1 tensor).
        return v2


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 2, 2)
