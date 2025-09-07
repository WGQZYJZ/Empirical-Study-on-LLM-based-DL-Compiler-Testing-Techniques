
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attn = torch.nn.Linear(512, 512)
        self.ln  = torch.nn.LayerNorm(512)
 
    def forward(self, xq, xk):
        q  = self.attn(xq) # Compute the linear output of the query
        k  = self.attn(xk)
        ln = self.ln(qk)  # Normalize the query and key tensors using a LayerNorm layer
        v = q * k + ln
        v = torch.nn.functional.dropout(v, p=dropout_p)
        return v
# Initializing the model
m  = Model()


