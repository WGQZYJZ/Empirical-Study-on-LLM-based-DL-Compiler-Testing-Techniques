 
class Model(torch.nn.Module):
    def __init__(self, conv, bn):
        super().__init__()
        self.conv = torch.nn.Conv2d(...) # ...

    def forward(self, x1):
        v1 = x1.permute(0, 2, 1)
        v2 = self.conv(v1) # Fusion will happen here
        v3 = torch.nn.functional.batch_norm(..., batch_first=True)
        return v3

# Initializing the model
m = Model(...)
