
class AttentionBlock(nn.Module):
    def __init__(self, dim, heads = 8, dim_head=64 ,dropout=0.1):
        super().__init__()
        self.heads = heads 
        self.scale = math.sqrt(dim_head)

        self.query = nn.Linear(dim, dim * self.heads)
        self.key = nn.Linear(dim, dim * self.heads)
        self.value = nn.Linear(dim, dim * self.heads)
        self.attn_drop = nn.Dropout(dropout)
        
    def forward(self, x):
        