
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1, x2):
        query = self.conv(x1)
        key   = self.conv(x2)
        return self.layer(query, key)
    
    @torch.jit.script_method
    def layer(self, query, key):
        