
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(3, 8, 1)
        self.conv2 = torch.nn.Conv2d(8, 8, 3, padding=1)
 
    def forward(self, x1, x2):
        x1 = F.leaky_relu(self.conv1(x1))
        x2 = F.leaky_relu(self.conv2(x2))
        qk  = (x1 * x2).sum(-1) / math.sqrt(x1.size(-1))
        qk  = F.softmax(qk, dim=-1)
        attn_weight  = self.conv2(qk).unsqueeze(dim=1) @ x1
        output = attn_weight @ x2
        return output


# Initializing the model
m = Model()

