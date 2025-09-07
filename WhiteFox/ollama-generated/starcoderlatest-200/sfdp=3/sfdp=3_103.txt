
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attention = torch.nn.MultiheadAttention()
 
    def forward(self, q1, k1, v1):
        x1, attn_scores  = self.attention(q1, k1, v1)
        scaled_attn_scores  = attn_scores.mul(scale_factor)
        softmax_attn_scores = scaled_attn_scores.softmax(dim=-1)
        dropout_attn_scores = torch.nn.functional.dropout(softmax_attn_scores, p=dropout_p)
        output_attn  = dropout_attn_scores.matmul(v1)
        return output_attn
 
# Initializing the model
m = Model()
 
# Inputs to the model
q1 = torch.randn(16, head_num*2, embed_dim)
k1 = torch.randn(16, head_num*2, embed_dim)
v1 = torch.randn(16, head_num*2, embed_dim)
