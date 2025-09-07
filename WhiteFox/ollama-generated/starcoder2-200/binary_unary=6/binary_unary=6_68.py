
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(4096, 256)
 
    def forward(self, x1):
        v1 = self.linear(x1)
        v3 = t3 - other_variable
        v4 = F.relu(v3)
        return v4


# Initializing the model and generating input tensor