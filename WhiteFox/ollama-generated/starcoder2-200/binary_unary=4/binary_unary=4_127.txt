
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(3, 20)

    def forward(self, x1, other): 
        v1 = self.linear(x1)
        v2 = v1 + other # Here you can pass a random tensor as the second argument to the `v1` operation. If you want, you can also set `other` as a keyword argument.
        v3  = torch.nn.functional.relu(v2)
        return v3


# Initializing the model
m  = Model()
# Setting random values for other parameter of forward method (here we use 4 as an example).
random_tensor  = torch.randn(10, 5) # 10 is batch size and 5 is size of feature map.
__output__  = m(torch.ones(32, 64), other=random_tensor)

