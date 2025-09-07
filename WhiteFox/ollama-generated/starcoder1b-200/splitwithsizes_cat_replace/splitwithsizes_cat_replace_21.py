
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1, x2):
        split_tensor_0 = torch.split(x1, [5], dim=-1)[0]
        concat_tensor  = torch.cat([split_tensor_0, x2], dim=-1)
        __output__   = self.conv(concat_tensor)
        return __output__


# Initializing the model
m = Model()

