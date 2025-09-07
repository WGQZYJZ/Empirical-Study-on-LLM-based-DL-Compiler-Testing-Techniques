
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.query  = torch.randn(32, 16, 8)
        self.key   = torch.randn(32, 4096, 8) 
        self.value = torch.randn(32, 4096, 8)
 
    def forward(self):
        m  = torch.einsum("bkd,bd->bk", (self.query , self.key)) / math.sqrt(self.query.size(-1)) 
        attn_mask  = torch.ones([32, 4096], dtype=torch.int) * (-math.inf)
        m[...,:10] += attn_mask[...: , :10]
        attn_weight  = F.softmax(m, dim=-1)
        output       = torch.einsum("bkd,dbk->bkt", (attn_weight , self.value))
        return output


# Initializing the model
m  = Model()

# Inputs to the model
__input1__, __input2__, __input3__ = torch.randn(32, 8), torch.randn(4096, 8), torch.randint(-math.inf , math.inf, (32, 4096))

# Model outputs
__output1__  = m()

