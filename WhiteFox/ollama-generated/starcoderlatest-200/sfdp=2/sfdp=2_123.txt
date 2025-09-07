
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.layer_norm = torch.nn.LayerNorm([128, 512])
        self.attention = torch.nn.Linear(128, 2048)
        self.dropout = torch.nn.Dropout(p=0.1)
 
    def forward(self, query, key):
        v1 = torch.matmul(query, key.transpose(-2, -1))
        v2 = v1 / 16
        softmax_v3 = F.softmax(v2, dim=-1)
        dropout_v4 = self.dropout(softmax_v3)
        attention_v5 = dropout_v4.matmul(self.attention(self.layer_norm(query + key))).transpose(-2, -1)
        output = query + attention_v5
        return output


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
x2 = torch.randn(1, 3, 64, 64)
