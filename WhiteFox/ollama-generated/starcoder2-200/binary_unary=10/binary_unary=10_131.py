
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        return torch.relu(x1 + 3.) # Applying the ReLU function to the result of adding another tensor

