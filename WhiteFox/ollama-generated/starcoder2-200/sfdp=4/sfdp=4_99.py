
import torch
class Transformer(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
        self.query  = torch.nn.Linear(32, 64) 
        self.key    = torch.nn.Linear(32, 128)
        self.value  = torch.nn.Linear(32, 96)
        self.linear = torch.nn.Linear(750 + 96*32 - 32 * 48 + 48 * 32, 2)
 
    def forward(self, x1):
 
        qk_a = self.query(x1).transpose(-2,-1)
        key = self.key(x1)
        value=self.value(x1)
         
        attn_mask=torch.ones((48,48), dtype=torch.float32)
        attn_mask.fill_(float('-inf'))
        attn_mask = attn_mask.masked_fill(attn_mask, 0).masked_fill(~attn_mask, -1e9)
 
        qk=(qk_a @ key.transpose(-2,-1))/math.sqrt(query.size(-1))
        qk+= attn_mask
        attn_weight=torch.softmax(qk,dim=-1)
 
        output = attn_weight @ value 
        return output, attn


# Initializing the model 
m = Transformer() 

# Inputs to the model 
x1 = torch.randn((48*32),requires_grad = True).view(-1,48 ,32)
 
__output__,__attn__= m(x1)

