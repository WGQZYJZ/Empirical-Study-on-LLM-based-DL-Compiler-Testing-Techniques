
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1)
        self.bn1 = nn.BatchNorm2d(8)
        self.bn2 = nn.BatchNorm2d(8)
        self.attn = nn.Linear(8, 1)
 
    def forward(self, x):
        x = self.conv(x)
        x = self.bn1(x)
        x = F.relu(x)
        x = self.bn2(x)
        x = F.relu(x)
        attn_weight = torch.softmax(self.attn(x), dim=-1)
        output = torch.einsum('bc,bch->bche', (attn_weight, x))  # Compute the dot product of the attention weights and the value
        return output


# Initializing the model
m = Model()


