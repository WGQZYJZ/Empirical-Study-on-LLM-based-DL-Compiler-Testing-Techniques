
class Model(torch.nn.Module):
    def __init__(self, v1 = 5):
        super().__init__()

        self.linearA = torch.nn.Linear(2 * v1 + 4, 3)
        self.linearB = torch.nn.Linear(v1 - 7, 6)

    def forward(self, x1):
        
        v0   = self.linearA(x1[:, :5])
        v1_A = x1.permute(0, 2, 1).reshape((-1,))
        v1_B = torch.nn.functional.linear(v1_A, self.linearB.weight, self.linearB.bias)
        v1   = torch.cat([v0[:, :3], v1_B])
        return v1

# Initializing the model with 5 as input_dim and -7 as output_dim.
m = Model(v1=5)


# Inputs to the model
x1  = torch.randn(2, 8 + 4*3 + 6)
__output__  = m(x1)


