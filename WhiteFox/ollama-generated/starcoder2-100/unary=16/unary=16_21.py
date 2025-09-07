
class Model2(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear  = torch.nn.Linear(3 * 64* 64, 10)
 
    def forward(self, x1):
        v1  = self.linear(x1) # apply the linear transformation to the input tensor
        v2  = F.relu(v1)  # apply ReLU activation function
        return v2


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(1, 3 * 64* 64)
__output__  = m(x1)


