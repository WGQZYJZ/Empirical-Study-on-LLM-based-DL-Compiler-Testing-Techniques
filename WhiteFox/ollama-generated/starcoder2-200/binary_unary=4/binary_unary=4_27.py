
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        v = torch.nn.functional.linear(x1) + 63 # Add another tensor to the result of applying a linear transformation to the input
        v = F.relu(v)

# Initializing the model