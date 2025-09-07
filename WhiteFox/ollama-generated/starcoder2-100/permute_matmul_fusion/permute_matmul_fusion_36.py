
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        v1  = torch.randn(1, 3)

        # For testing both cases. Please only choose one
        t2a = v1.permute([0, 2]).transpose() 
        t2b = v1.permute([0, 2])
        t3  = torch.matmul(t2a, t2b)

        return [v1]


# Initializing the model
m = Model()

# Inputs to the model
x1_a  = torch.randn(3)
x1_b  = torch.randn(50).view(-1, 784)
__output__  = m([x1])


