
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        inv_scale = 1 / (torch.norm(v1, dim=-1).unsqueeze(-1))
        attention_weights = torch.matmul(v1.transpose(-2, -1), x1).softmax(-1) * inv_scale
        output = attention_weights.matmul(x1)
        return output


# Initializing the model
m = Model()

