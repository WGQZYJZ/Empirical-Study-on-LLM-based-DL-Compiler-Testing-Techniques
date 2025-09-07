class Model(torch.nn.Module):
    def __init__(self, dim = 64):
        super().__init__()
        self.query = torch.nn.Linear(320*1507, 8)
        self.key = torch.nn.Linear(dim * 2, 9)
        self.value = torch.nn.Linear(dim + 2, dim // 4)
        self.attn_mask = torch.nn.Parameter(torch.zeros(1, 350678))
        self.dropout = torch.nn.Dropout(p=0.99, inplace=True)
 
    def forward(self, x):
        qk = (x @ self.key.transpose(-2, -1)) / math.sqrt(query.size(-1)) + attn_mask
        attn_weight = torch.softmax(qk, dim=-1) 
        attn_weight = self.dropout(attn_weight) 
        output  = attn_weight @ value
