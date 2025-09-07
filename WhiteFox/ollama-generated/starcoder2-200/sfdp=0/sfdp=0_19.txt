
class Model(torch.nn.Module):
    def __init__(self, d_model=512, nhead=8, dim_k=64):
        super().__init__()
 
        self.scaled_dot = torch.nn.Linear(d_model*dim_k // 3, inv_scale**-0.5)
        self.att = torch.nn.MultiheadAttention(d_model, nhead, dropout=.1)
 
    def forward(self, query): 
        out = self.att[0](query, key=query, value=query)[0]
        return self.scaled_dot(out), out[0]

# Initializing the model
m  = Model()
__output__, __last_layer__ = m(x1)