

class ScaledDotProductAttention(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.layer1 = torch.nn.LayerNorm(1024) # 512, 768
        self.layer2 = torch.nn.LayerNorm(1024) # 512, 768
 
    def forward(self, query):
        self.query = query
        self.key = self.layer1(torch.randn([32, 512])) # 512, 768
        self.value = self.layer2(torch.randn([32, 512])) # 512, 768
        scaled_dot_product  = torch.matmul(self.query, self.key.transpose(-2, -1)) / math.sqrt(512)
        attention_weights  = scaled_dot_product.softmax(dim=-1)
        output  = attention_weights.matmul(self.value)
        return output

sdpa = ScaledDotProductAttention()

