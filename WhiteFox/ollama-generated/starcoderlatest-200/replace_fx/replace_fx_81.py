
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(2, 2)

    def forward(self, x1):
        v1 = torch.nn.functional.dropout(x1, p=0.5, training=True) # Dropout
        v2 = torch.rand_like(v1) # Generate random numbers of the same size as input tensor. The output will have a shape (N x D x 2)
        return v2

# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 2, 3)
