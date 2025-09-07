
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(2, 2)

    def forward(self, x1):
        v1 = x1.permute(0, 2, 1)
        v2 = torch.nn.functional.linear(v1, self.linear.weight, self.linear.bias)
        return v2


# Initializing the model
m1 = Model()
m2 = Model()
m3 = Model()

## Initializing the inputs to the models
x1  = torch.randn(1, 2, 2)
x2  = torch.randn(1, 3, 2)
x3  = torch.randn(1, 4, 2)


## Expected outputs of both models
y1 = m1(x1) # [1 x 2 x 2]
y2 = m2(x2) # [1 x 3 x 2]
y3 = m3(x3) # [1 x 4 x 2]


