
class Model(torch.nn.Module):
    def __init__(self, nhead, attn_dropout):
        super().__init__()
        self.nhead = nhead
        self.attn_drop = nn.Dropout(attn_dropout)
        self.fc1 = nn.Linear(256, 768)
        self.fc2 = nn.Linear(768, 256)
        self.out = nn.Linear(256, nhead * 3)

    def forward(self, x1):
        v1 = torch.nn.functional.adaptive_avg_pool2d(x1, (256))
        v1 = F.relu(self.fc1(v1.view(-1, 256)))
        v2 = self.attn_drop(v1)
        v3 = self.fc2(v2)
        v4 = torch.nn.functional.adaptive_avg_pool2d(F.relu(v3), (7, 7))
        output = self.out(v4.view(-1, 256)).transpose(1, -1).contiguous()

        return output

# Initializing the model
m = Model(4, 0.1)

# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
