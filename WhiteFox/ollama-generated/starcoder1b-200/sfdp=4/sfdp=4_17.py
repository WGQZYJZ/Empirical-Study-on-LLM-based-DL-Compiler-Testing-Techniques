
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        attn_mask = (x1 == x1).float() # The attention mask should only affect the position of the non-padding values of the input tensor
        v1    = self.conv(x1)
        v2    = v1  * 0.5
        v3    = v1  * 0.7071067811865476
        v4    = torch.erf(v3)
        v5    = v4 + 1
        v6    = v2  * v5
        return v6, attn_mask


# Initializing the model
m = Model()


