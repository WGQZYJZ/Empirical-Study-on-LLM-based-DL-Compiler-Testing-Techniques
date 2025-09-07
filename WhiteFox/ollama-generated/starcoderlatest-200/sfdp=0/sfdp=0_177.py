
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear_layer1 = torch.nn.Linear(768, 2048)
        self.attention_dropout = torch.nn.Dropout(p=0.3)
        self.layer_norm = torch.nn.LayerNorm([768])
 
    def forward(self, x):
        v1 = self.linear_layer1(x)
        v2 = self.attention_dropout(v1)
        v3 = self.layer_norm(v1 + v2)  # Adding two layers to the model
        return torch.matmul(v3, self.v4)
 
class ModelWithScaledDotProductAttention(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear_layer1 = torch.nn.Linear(768, 2048)
        self.attention_dropout = torch.nn.Dropout(p=0.3)
        self.layer_norm = torch.nn.LayerNorm([768])
        self.scaled_dot_product_attention = ScaledDotProductAttention()
 
    def forward(self, x):
        v1 = self.linear_layer1(x)
        v2 = self.attention_dropout(v1)
        v3 = self.layer_norm(v1 + v2)  # Adding two layers to the model
        return self.scaled_dot_product_attention(q, k, v4)
 
