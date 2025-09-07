
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        t1 = torch.nn.functional.dropout(x1, 0.3) # Apply dropout to the input tensor with probability 0.3
        t2 = torch.rand_like(t1, 64*50, dtype=torch.float).to("cuda") # Generate a random tensor of size [1, 2]
        return t1 + t2


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(1, 2)


