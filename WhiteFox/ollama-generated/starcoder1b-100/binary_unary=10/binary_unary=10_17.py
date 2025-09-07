
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear  = torch.nn.Linear(10, 8)

    def forward(self, x1):
        v1 = self.linear(x1) + torch.ones(x1.shape, dtype=torch.float32, device=x1.device) # Add some random noise to the input tensor
        return relu(v1)


# Inputs to the model
x1  = torch.randn(1, 10)
