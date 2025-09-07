
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = v1 - other
        v3 = F.relu(v2)
        return v3


# Initializing the model
m = Model()
 
# Inputs to the model 
x1 = torch.randn(1, 3, 64, 64)
other = [0] if torch.__version__ == '1.7' else [] #  For the backward compatibility with PyTorch <= 1.8, there is no parameter "other" in function `v2 - other`. For the backward compatibility with PyTorch >= 1.9, this line should be removed
 
