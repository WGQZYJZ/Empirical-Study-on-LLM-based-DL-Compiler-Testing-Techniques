
class Model2(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(3, 5)
 
    def forward(self, x1, x2):
        v1 = self.linear(x1) + x2  # Add x2 to the output of a linear transformation
        v2 = F.relu(v1 - other)
        return v2
