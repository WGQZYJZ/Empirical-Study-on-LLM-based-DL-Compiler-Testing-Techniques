
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.qkv_attention = torch.nn.Linear(d_model, d_model*3)
 
    def forward(self, q, k, v):
        attn_weights = self.qkv_attention(torch.cat((q, k, v), dim=-1))
        softmax_attn_weights = attn_weights.softmax(dim=-1)
        output = torch.nn.functional.dropout(softmax_attn_weights, p=dropout_p)
        return torch.matmul(output, v)

 # Initializing the model
m = Model()
 
 # Inputs to the model
q  = torch.randn(1, 32, d_model)
k = torch.randn(8, 32, d_model)
v  = torch.randn(8, 32, d_model)
