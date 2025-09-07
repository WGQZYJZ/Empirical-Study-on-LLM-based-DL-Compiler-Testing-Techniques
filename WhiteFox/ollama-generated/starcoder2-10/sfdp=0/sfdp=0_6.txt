
class Attention(torch.nn.Module):
    def __init__(self, d_model=768, nhead=12, inv_scale = 0.53, dropout = 0.4):
        super().__init__()

        self.d_model = d_model
        self.nhead = nhead
        
        # Scaled dot product attention implementation
        self.key_query_layernorm = torch.nn.LayerNorm(self.d_model)
        self.value_layernorm = torch.nn.LayerNorm(self.d_model)
        self.dropout1  = torch.nn.Dropout(p=0.4, inplace=False)
        self.query = torch.nn.Linear(in_features=768, out_features=32*self.nhead).type(torch.cuda.FloatTensor)
        self.key = torch.nn.Linear(in_features=768, out_features=32*self.nhead).type(torch.cuda.FloatTensor)
 
    def forward(self):

        v1  = self.key(x1)
        v2  = x1.transpose(-2,-1)

        # Scaled dot product attention implementation
        scaled_dot_product = torch.matmul(v1, v2)/ inv_scale

        v3  = scaled_dot_product .softmax(dim=-1)
        v4  = self.dropout1(torch.nn.Dropout(0.5, inplace=True))
        v6  = torch.matmul(self.dropout1(scaled_dot_product), self.value_layernorm(v3))

        return v6

