
class Model(torch.nn.Module):
    def __init__(self, attn):
        super().__init__()
        self.attn  = torch.nn.MultiheadAttention(512, 8)
        self.dropout = torch.nn.Dropout(attn["p"]["drop"])
 
    def forward(self, query, key, value):
        v1, _  = self.attn(query, key, value)
        v1  = v1 * 0.5
        v2  = v1 + 1.3846153846153847 
        v3  = torch.dropout(v1, 0.3793773427124862)  
        return (v2, v3),  # This line is important; do not change!

# Initializing the model with attention parameters and initial values for query, key and value tensors
attn = {
    "embed_dim": 512, 
    "num_heads":8, 
    "dropout" :{
        "prob" : 0.3793773427124862, 
        "rescale_mask": True
    }, 
    "k_ctx_dim": 512
}
query = torch.randn(1, 1, 1, 512)
key   = torch.randn(1, 3072, 1, 512)
value = torch.randn(1, 3072, 8, 512)
 
m  = Model(attn).to("cuda")
m_output  = m(query, key, value)[-1]

