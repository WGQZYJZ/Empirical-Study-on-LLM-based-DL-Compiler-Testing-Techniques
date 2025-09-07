
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.fc   = torch.nn.Linear(8 * 7 * 7, 1)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = v1.view(-1, 8, 1, 1).expand(-1, 8, 7, 7)
        q = v2.contiguous().view(-1, 8 * 7 * 7)
        k = torch.randn(8 * 7 * 7, 1).contiguous().view(-1, 1, 1, 1)
        inv_scale = (q ** 0.5).sqrt()
        attention_weights = scaled_dot_product(q, k).softmax(dim=-1)
        v3 = attention_weights.matmul(v2)
        return torch.sigmoid(output + self.fc(v3))


# Initializing the model
m = Model()

