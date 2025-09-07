
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear  = torch.nn.Linear(10, 20)
 
    def forward(self, x1, other=None):
        v1 = self.linear(x1)
        if other is None:
            other = torch.tensor([1])
        else:
            other = torch.tensor([0], requires_grad=False).to(other) # Create a new tensor with zeros and requires grad disabled
        return v1 + other


# Initializing the model
m  = Model()


# Inputs to the model
x1 = torch.randn(1, 10)
other = torch.randn(1, 20, dtype=torch.int64)
