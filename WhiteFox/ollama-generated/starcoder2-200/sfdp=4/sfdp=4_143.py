
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
        self.query  = torch.randn([2, 3])
        self.key  = torch.randn([16, 8, 4, 4])
        self.value  = torch.randn([10, 7, 5])
        self.attn_mask  = torch.randn([32, 8])
 
    def forward(self):
        qk  = query @ key.transpose(-2, -1) / math.sqrt(query.size(-1))
        qk  = qk + attn_mask
 
        attn_weight  = torch.softmax(qk, dim=-1)
        output  = attn_weight @ value


# Initializing the model
m  = Model()

