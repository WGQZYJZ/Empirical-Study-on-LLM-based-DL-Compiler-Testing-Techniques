
class Model(torch.nn.Module):
    def __init__(self, channel_number=3, hidden_channel_number=8):
        super().__init__()
        self.conv = torch.nn.Conv2d(channel_number, hidden_channel_number, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = v1 * 0.5
        v3 = v1 * 0.7071067811865476
        v4 = torch.erf(v3)
        v5 = v4 + 1
        v6 = torch.addmm(v2, torch.eye(hidden_channel_number).unsqueeze(1), torch.eye(hidden_channel_number))
        return v6


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
