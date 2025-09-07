
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear  = torch.nn.Linear(64 * 25, 1)

    def forward(self, x0, x1):

        # Concatenate two tensors
        v3  = torch.cat([x0, x1], dim=0)
        v4  = v3 / 8 
        v5  = self.linear(v4).view(-1)
        v6  = F.relu(v5 + 2.)
        return v6


# Initializing the model
m  = Model()

# Inputs to the model
x0  = torch.randn(3, 64 * 25 // 8).requires_grad_()
x1  = torch.zeros(3, 64)

__output__  = m(x0, x1)

