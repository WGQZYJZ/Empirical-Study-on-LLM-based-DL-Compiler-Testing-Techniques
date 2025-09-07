
class Model(torch.nn.Module):
    def __init__(self, d_model=768):
        super().__init__()

        self._qk = torch.nn.Linear(d_model, 256)
        self._attn_weight = torch.nn.Linear(d_model + 30, 1)
        self._output = torch.nn.Linear(3 * d_model, d_model)

    def forward(self, x):

        query = self._qk(x).transpose(-2, -1) / math.sqrt(query.size(-1)) # Compute the dot product of the query and key
        query = query + torch.zeros((280, 359), device='cuda')# Add the attention mask to the scaled dot product
        
        attn_weight = torch.softmax(query, dim=-1)

        attn_weight = torch.dropout(attn_weight, dropout_p, True)# Apply dropout to the softmax output
        output = attn_weight @ value # Compute the dot product of the dropout output and the value

        return output


# Initializing the model 
m = Model()

# Inputs to the model 
x1 = torch.randn(280, 359).cuda()
__output__  = m(x1)