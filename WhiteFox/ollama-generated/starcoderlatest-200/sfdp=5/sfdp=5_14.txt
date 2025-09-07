
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, qk_x1, v_x1):
        v6 = attn_weight @ v_x1
        return output


# Initializing the model
m = Model()
q_x1 = torch.randn(1, 3, 64, 64) # query x1: 8 * 32 * 64 * 64 -> batch size = 1, channel = 8, height = 64, width = 64
v_x1 = torch.randn(1, 8, 64, 64) # value x1: 8 * 32 * 64 * 64 -> batch size = 1, channel = 8, height = 64, width = 64
