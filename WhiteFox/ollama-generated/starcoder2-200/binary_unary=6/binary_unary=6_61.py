
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(8096, 128)
 
    def forward(self, x1):
        v1  = self.linear(x1) # Applying a linear transformation to the input tensor 
        v4 = torch.relu(v3 - 5.71e-5)
        return v4
