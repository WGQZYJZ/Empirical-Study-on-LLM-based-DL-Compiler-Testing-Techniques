
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(1, 3)
 
    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = v1 + other_tensor
        return v2

# Initializing the model and other tensor with random data
m = Model()
other_tensor = torch.randn(4096,)


# Inputs to the model, where `v1` is `m(x1)` as specified in the previous test case.
x1 = v1 + 2*torch.rand([5,3])

# Initializing other tensor with random data
other_tensor = torch.randn(4096,)


# Inputs to the model, where `v1` is `m(x1)` as specified in the previous test case.
x1  = v1 + 2*torch.rand([5,3])

