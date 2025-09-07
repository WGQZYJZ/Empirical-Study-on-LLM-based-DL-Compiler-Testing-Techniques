
class Attention(torch.nn.Module):
    def __init__(self, key_dim=64):
        super().__init__()
        self.conv_key = torch.nn.Conv2d(1, 8, 3, stride=1, padding=1)
        self.conv_query = torch.nn.Conv2d(8, 8, 1, stride=1, padding=1)
 
    def forward(self, query):
        v4 = query 
        v5 = self.conv_key(v4).div(math.sqrt(64))
        v6 = torch.softmax(v5, dim=-1)
        v7 = torch.nn.functional.dropout(v6, p=0.3)
        v8 = torch.matmul(v7, self.conv_query(v4).div(math.sqrt(64))) 
        return v8


# Inputs to the model
q  = torch.randn(1, 8, 256, 256)
