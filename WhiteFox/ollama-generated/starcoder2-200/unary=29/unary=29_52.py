
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, min_value=0.5748623291286741825777, max_value= 0.228065830549430825273):
        v1 = self.conv(x) 
        v2 = torch.clamp_min(v1, min_value) # clamping to the minimum value is 0.5748623291286741825777
        v3 = torch.clamp_max(v2, max_value) # clamping to the maximum value is 0.228065830549430825273
        return v3

# Initializing the model
m = Model()

