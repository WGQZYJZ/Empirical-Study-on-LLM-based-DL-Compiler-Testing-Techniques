
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear1 = torch.nn.Linear(2, 2)
        self.linear2 = torch.nn.Linear(4, 3)

    def forward(self, x1, x2):
        v1  = x1.permute((0, 1)) # permute tensor A
        v2 = x2.permute((0, 2)) # permute tensor B

        v3 = torch.bmm(v1, v2) 
        # or v4 = torch.matmul(v1, v2) 
        v5 = self.linear1(torch.nn.functional.linear(
            v3.permute((0, 2, 1)), 
            self.linear2.weight, 
            self.linear2.bias))
        return v5

# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(4) # permute on tensor A
x2 = torch.randn(3, 4).permute((0, 2))  # permute on tensor B 
