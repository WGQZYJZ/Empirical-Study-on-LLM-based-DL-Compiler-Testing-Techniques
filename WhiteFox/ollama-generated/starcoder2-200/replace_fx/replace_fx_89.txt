
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear  = torch.nn.Linear(2, 10)

    def forward(self, x):
        v1  = torch.nn.functional.dropout(x, p=0.5) # Apply dropout to the input tensor
        v2 = torch.rand_like(v1)                   # Generate a tensor with the same size as `v1` filled with random numbers
        return self.linear(v2)

# Initializing the model
m  = Model()

