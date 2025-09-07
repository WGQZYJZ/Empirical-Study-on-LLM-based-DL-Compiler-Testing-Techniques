
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1, y2):
        v1 = self.conv(x1, y2) # Splitting along the first dimension of input_tensor and concatenation along the second dimension
        v2 = torch.cat([v1, x1], dim=0) # Concatenating split tensors along the second dimension
        return v2


# Initializing the model
m = Model()


