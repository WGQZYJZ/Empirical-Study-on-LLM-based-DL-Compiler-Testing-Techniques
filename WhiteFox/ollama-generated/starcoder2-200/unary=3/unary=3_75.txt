
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = v1 * 0.5 
        v3 = v1 + -1
        v4 = v3 * v2 # add -1 to the output of pointwise convolution
        return v4

# Initializing the model with torch.load_state_dict
m  = Model()
state_dict = torch.load(file_path_state_dict, map_location=device)
m.load_state_dict(state_dict)
m


# Inputs to the model
x1  = torch.randn(batch_size, 3, 64, 64)
__output__  = m(x1)

