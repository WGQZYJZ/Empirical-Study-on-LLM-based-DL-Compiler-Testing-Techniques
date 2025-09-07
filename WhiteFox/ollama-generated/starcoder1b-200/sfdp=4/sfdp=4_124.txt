
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        attn_mask = torch.zeros(x1.shape[0], x1.shape[1], x1.shape[2] // 4, device=x1.device, requires_grad=False)
        qk  = self.conv(x1) * math.sqrt(qk.size(-1))
        attn_weight = torch.softmax(qk, dim=-1)
        output = attn_weight @ value
        return output

# Initializing the model
m = Model()


