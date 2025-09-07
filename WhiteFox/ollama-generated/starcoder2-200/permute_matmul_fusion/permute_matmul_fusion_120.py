

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1, x2):
         v = torch.bmm(x1.permute(0, 2, 1), x2) # swap dimensions of the first input tensor and the second input tensor
         return v

# Initializing the model