
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear1 = torch.nn.Linear(2, 2)

    def forward(self, x1):
        v1 = x1.permute(0, 3, 1).permute(0, 3, 2) 
        v2 = torch.bmm(v1, self.linear1.weight, self.linear1.bias) # or you can use torch.matmul
        return v2

# Initializing the model
m = Model()


# Inputs to the model