

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear  = torch.nn.Linear(2, 3)

    def forward(self, x1):
        v1  = torch.nn.functional.dropout(x1, 0.5) # Apply dropout to the input tensor with p=0.5 
        v2  = torch.rand_like(v1)    # Generate a random tensor with the same size as t1 filled with random numbers
        return self.linear(v2)

# Initializing the model
m  = Model()

# Input tensors for the model to be executed
x1  = torch.randn(3, 2)

