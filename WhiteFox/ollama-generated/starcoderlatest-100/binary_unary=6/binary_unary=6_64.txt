
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(3, 8)
 
    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = v1 - other_const
        v3 = relu(v2)
        return v3


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
other_const = 0.5 * x1 + 0.7071067811865476 * x2 + torch.rand_like(v3) # 'other' is replaced by random values generated for each batch element in the format of (x1*0.5, x2*0.7071067811865476, v3)
