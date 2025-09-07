
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
 
        v1  = torch.nn.functional.conv_transpose2d(x1, self.kernel, output_size=5)
 
        return torch.sigmoid(v1)

# Initializing the model
m = Model()
