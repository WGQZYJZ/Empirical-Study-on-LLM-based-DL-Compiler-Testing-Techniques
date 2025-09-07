
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(2, 2)

    def forward(self, x1, x2):
        v1 = torch.bmm(x1, x2) # Bmm is used on tensor A and B (as defined in the input model)
        v2 = torch.matmul(x1, x2) # Matmul is used on tensor A and B (as defined in the input model)
        return v1 + v2


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(2, 2, 2)
x2 = torch.randn(2, 2, 2)
