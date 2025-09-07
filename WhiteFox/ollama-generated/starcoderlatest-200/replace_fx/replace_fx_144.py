
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(2, 3)

    def forward(self, x1):
        v1 = torch.nn.functional.dropout(x1, p=0.5) # Dropout the input tensor with a probability of 0.5. 
        v2 = torch.rand_like(v1)                         # Generate a tensor with the same size as input tensor filled with random numbers. 
        return self.linear(v1 + v2)


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(1, 3, 2)
