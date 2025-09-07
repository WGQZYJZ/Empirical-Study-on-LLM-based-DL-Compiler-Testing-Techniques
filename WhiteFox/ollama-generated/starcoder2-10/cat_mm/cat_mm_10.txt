
class Model(torch.nn.Module):
    def __init__(self, input1_length=30, input2_length=45):
        super().__init__()
 
        self.input1 = torch.randn((10 * 30, ))
        self.input2 = torch.randn((8 * 45,))

    def forward(self, x):
        v1 = torch.mm(x.reshape(-1), y)
        v2 = torch.cat([v1] + [v1 for _ in range(7)], -1) 
        return v2


# Initializing the model
m  = Model()

# Inputs to the model
x1_length, x2_length  = 30, 45 # These two numbers should be different from previous model's two numbers.
x1 = torch.randn(7 * x1_length)
x2 = torch.randn(8 * x2_length)
x3 = torch.cat([x1] + [x1 for _ in range(6)])

