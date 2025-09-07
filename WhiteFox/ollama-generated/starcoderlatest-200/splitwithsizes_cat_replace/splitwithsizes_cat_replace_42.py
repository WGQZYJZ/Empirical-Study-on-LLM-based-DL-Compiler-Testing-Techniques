
class Model(torch.nn.Module):
    def __init__(self, dim=2):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = v1 * 0.5
        v3 = v1 * 0.7071067811865476
        v4 = torch.erf(v3)
        v5 = v4 + 1
        v6 = v2 * v5
        return v6

# Splitting the model input tensor to four tensors
x1_split1, x1_split2, x1_split3, x1_split4 = torch.split(x1, split_sizes=[2, 4, 8, 16], dim=1)
 
# Concatenating the four splitted tensors to form the new input tensor for the model (shape is [8, 16])
x_new_input = torch.cat([x1_split1, x1_split2, x1_split3, x1_split4], dim=0)
 
# Initializing the model
m = Model()

# Inputs to the model
__output__  = m(x_new_input)
