
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(20, 10)
 
    def forward(self, x1):
        v1 = self.linear(x1) * 0.5
        v2 = torch.tensor([[0], [1]], device='cuda') + v1
        v3 = (v2 * v2 * v2).mul(0.044715).sqrt()
        v4 = v3.mul_(v3)
        v5 = (torch.tanh(v4)).add_(1)
        v6 = v2 * v5
        return v6


# Initializing the model
m = Model()

# Inputs to the model
x1  = torch.randn(3, 10)
