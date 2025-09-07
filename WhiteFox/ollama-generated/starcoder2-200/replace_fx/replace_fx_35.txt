

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear  = torch.nn.Linear(2, 2)

    def forward(self, x1):
        v3 = torch.nn.functional.dropout(x1, p=0.5) # Apply dropout to the input tensor
        v4 = torch.rand_like(v3) # Generate a tensor with the same size as the permuted one filled with random numbers
        return v4

# Initializing the model
m  = Model()

