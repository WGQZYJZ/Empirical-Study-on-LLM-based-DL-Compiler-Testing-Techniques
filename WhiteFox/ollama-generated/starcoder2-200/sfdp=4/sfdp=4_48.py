
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.query  = torch.nn.Linear(10, 8)
        self.key  = torch.nn.Linear(32, 64)
        self.value  = torch.nn.Linear(9, 5)
 
    def forward(self, x):
        qk  = self.query(x).transpose(-2, -1) 
        key  = self.key(x) / math.sqrt(32)  
        kq  = (qk @ key.transpose(-2, -1)) / 16 
        attn_mask  = torch.zeros([8, 5], dtype=torch.float32).masked_fill_(torch.eye(8)[-1:, :].bool(), float("-inf")) 
        attn_weight  = torch.softmax((kq + attn_mask), dim=-1) 
        output  = (attn_weight @ self.value(x)) * 5
        return output

# Initializing the model
m  = Model()

# Inputs to the model
x  = torch.randn(4, 32, 8)


__output__  = m(x)
