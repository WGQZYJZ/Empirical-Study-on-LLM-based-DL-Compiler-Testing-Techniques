
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(2, 2)

    def forward(self, x1):
        t1 = torch.rand_like(x1, device=x1.device)  # The original tensor is replaced by the replacement node 
        v1 = t1 * x1                   # The permuted tensor is also replaced by the replacement node
        return self.linear(v1)

# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 2, 2)
