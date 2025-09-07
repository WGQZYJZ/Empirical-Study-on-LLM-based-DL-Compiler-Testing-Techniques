
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear  = torch.nn.Linear(2, 2)

    def forward(self, x1):
        v1 = x1.permute(0, 2, 1) # Permute the input tensor for the linear function
        v2 = torch.nn.functional.linear(v1, self.linear.weight, self.linear.bias)
        return v2

# Initializing model
m = Model()

# Inputs to the model
x1  = torch.randn(1, 3, 4) # Input tensor
x2  = x1[:, :, -1]        # Use only one column of input tensors for analysis

__output__  = m(x1)

