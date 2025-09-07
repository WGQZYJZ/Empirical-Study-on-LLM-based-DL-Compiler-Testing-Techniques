
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear  = torch.nn.Linear(2, 1)

    def forward(self, x1):
        v1  = x1.permute(0, 2, 1).reshape(-1, 3) # Reshape the permuted tensor to a vector of size 6.
        v2  = torch.nn.functional.linear(v1, self.linear.weight, self.linear.bias)
        return v2


# Initializing the model
m  = Model()


# Inputs to the model
x1  = torch.randn(10, 3, 2) # Input tensors for the model. The tensor size is 60 by 6.
__output__  = m(x1)