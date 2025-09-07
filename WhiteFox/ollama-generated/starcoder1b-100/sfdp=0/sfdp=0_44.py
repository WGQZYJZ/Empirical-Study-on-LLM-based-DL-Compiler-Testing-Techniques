
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        scale  = torch.sqrt(torch.max(torch.abs(v1), dim=-1)[0])
        inv_scale  = 1 / scale
        query    = v1 * scale
        key      = x1 * scale
        attention_weights  = torch.matmul(query, key.transpose(-2, -1)) / inv_scale
        output   = attention_weights.matmul(value)
        return output


# Initializing the model
m = Model()

