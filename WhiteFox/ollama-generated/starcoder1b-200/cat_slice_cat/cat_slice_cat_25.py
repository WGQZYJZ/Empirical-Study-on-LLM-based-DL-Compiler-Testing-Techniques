
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, x2, x3):
        x4 = torch.cat([x1, x2, x3], dim=1)  # Concatenate the original concatenated tensor and the sliced tensor along dimension 1
        return x4


# Initializing the model
m = Model()

