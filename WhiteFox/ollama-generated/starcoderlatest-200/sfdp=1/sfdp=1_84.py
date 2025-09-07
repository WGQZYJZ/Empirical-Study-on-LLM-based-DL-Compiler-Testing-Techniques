
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
        self.q_proj = torch.nn.Linear(16, 256)
        self.k_proj = torch.nn.Linear(48, 256)
        self.v_proj = torch.nn.Linear(96, 256)
        self.o_proj = torch.nn.Linear(256, 768)
 
    def forward(self, q1, k1, v1):
        qk = torch.matmul(q1, k1.transpose(-2, -1))
        scaled_qk = qk.div(inv_scale_factor)
        softmax_qk = scaled_qk.softmax(dim=-1)
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=dropout_p)
        output = dropout_qk.matmul(v1)
 
        return self.o_proj(output)


# Inputs to the model
q1 = torch.randn(32, 16, 512) # query tensor
k1 = torch.randn(32, 48, 512) # key tensor
v1 = torch.randn(32, 96, 512) # value tensor
 
