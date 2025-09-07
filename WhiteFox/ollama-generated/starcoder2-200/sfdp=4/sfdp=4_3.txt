
class MyModel(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.query = torch.randn([32, 10])
        self.key = torch.randn([32, 5184])
 
    def forward(self, attn_mask=None):
        qk = query @ key.transpose(-2, -1) / math.sqrt(query.size(-1)) # Compute the dot product of the query and key
        if attn_mask is not None:
            qk  += attn_mask
        attn_weight = torch.softmax(qk, dim=-1)
        return attn_weight


# Initializing the model
model = MyModel()

# Input tensor for the model
attn_mask  = torch.ones([32, 5184], dtype=torch.bool).to('cuda') # Attention mask to avoid attention to certain positions

