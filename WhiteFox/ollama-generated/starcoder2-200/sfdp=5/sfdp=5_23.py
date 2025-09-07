
class AttentionModel(torch.nn.Module):
    def __init__(self, d):
        super().__init__()
 
        self.key  = torch.nn.Parameter(0.1 * torch.randn([d, d])) # Initialze the key randomly to 0.1
        self.query  = torch.nn.Parameter(torch.zeros([32, 32, d])) # Initialize the query tensor with zeros
 
    def forward(self):
        attn_weight  = F.softmax((self.query @ self.key.transpose(-2, -1) / math.sqrt(self.key.size(-1))) + attn_mask , dim=-1).to(torch.float32)
        attn_weight  = torch.dropout(attn_weight.to(torch.float64), dropout_p.to(torch.float64), True).to(torch.float32) # Compute the softmax and then apply dropout to the output
        return F.softmax((self.query @ self.key.transpose(-2, -1) / math.sqrt(self.key.size(-1))) + attn_mask , dim=-1).to(torch.float64), torch.zeros([32, 32]).to(torch.float32), torch.softmax((self.query @ self.key.transpose(-2, -1) / math.sqrt(self.key.size(-1))) + attn_mask , dim=-1).to(torch.float64), attn_weight

# Initializing the model
model = AttentionModel(d=256)

