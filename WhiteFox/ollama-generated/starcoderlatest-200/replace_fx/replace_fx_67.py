
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(2, 2)

    def forward(self, x1):
        v1 = torch.rand_like(x1) # generate a tensor with the same size as input_tensor filled with random numbers
        v2 = torch.nn.functional.dropout(v1, p=0.5) # apply dropout to the random generated tensor
        return self.linear(v2)


# Initialize the model
m = Model()


# Inputs to the model
x1 = torch.randn(1, 2, 2)
