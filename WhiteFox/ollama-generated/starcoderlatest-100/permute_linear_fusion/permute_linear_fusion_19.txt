
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear1 = torch.nn.Linear(2, 3)
        self.linear2 = torch.nn.Linear(3, 4)

    def forward(self, x1):
        v1  = x1.permute(0, 2, 1) # Permute the input tensor
        v2 = torch.nn.functional.relu(v1)
        v3 = self.linear1(v2)
        v4 = self.linear2(v3)

        return v4
# Initializing the model
m = Model()

# Inputs to the model
x1  = torch.randn(1, 2, 2)
