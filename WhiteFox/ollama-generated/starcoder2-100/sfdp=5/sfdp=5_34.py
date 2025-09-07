
class MyModel(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, x2, x3=0):  # Input parameters with default value `x3` of 0 are added to the model.
        qk = torch.einsum('bmnc,bmjnc->bjmc', x1, x2) / math.sqrt(torch.size(-2))
        qk += torch.nn.functional.dropout(x3, True)
        attn_weight  =  torch.softmax(qk, -1)
        output       =  torch.einsum('bmjc, bmnc->bmc', attn_weight, x1) + attn_weight
        return output
