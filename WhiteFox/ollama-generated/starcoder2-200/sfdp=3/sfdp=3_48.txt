
class SelfAttention(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, query, key=None, value=None, scale_factor: float = 1.0, dropout_p: float = 0.0) -> torch.Tensor: 
        # The query and key arguments can be None if not used in the computation
        qk  = torch.matmul(query, key.transpose(-2, -1)) / math.sqrt(self.d_model) 
        scaled_qk  = qk * scale_factor
        softmax_qk = scaled_qk.softmax(dim=-1)

        # The dropout argument can be set to 0.0 if not used in the computation
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=dropout_p)
        output = dropout_qk.matmul(value) 

        return output

# Initializing a model
sa = SelfAttention()

 # Inputs to the model 
 q1  = torch.randn([2048, 768])
 k1  = torch.randn([512, 768])
 v1 = torch.randn([2048, 3*768])
 
 q1_res = sa(q1) 
 k1_res = sa(k1, value=v1)

 # Initializing a model that is not used in the computation
 sa2  = SelfAttention()
 sa2.eval()
