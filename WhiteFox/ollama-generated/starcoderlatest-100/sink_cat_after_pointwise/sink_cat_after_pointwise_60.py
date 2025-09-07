
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(2, 2)

    def forward(self, x1, x2):
        v1 = torch.cat([x1, x2], dim=0)
        v2 = v1.view((v1.size(0), -1)) # reshape concatenated tensor and set size for the view to be (-1)
        v3 = torch.nn.functional.relu(v2) # apply ReLU operation to reshaped tensor
        return v3

# Inputs to the model
x1 = torch.randn(5, 2, 2)
x2 = torch.randn(4, 2, 2)
