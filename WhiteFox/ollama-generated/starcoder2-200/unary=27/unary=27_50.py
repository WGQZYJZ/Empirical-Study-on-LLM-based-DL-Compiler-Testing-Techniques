
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1  = self.conv(x1) 
        v2  = torch.clamp_min(v1, min_value=0.05) # clamping the output to a minimum value (0.05 in this example). 
        v3  = torch.clamp_max(v2, max_value=76.49832811800558)# clamping the output to a maximum value (76.49832811800558 in this example). 
        return v3
