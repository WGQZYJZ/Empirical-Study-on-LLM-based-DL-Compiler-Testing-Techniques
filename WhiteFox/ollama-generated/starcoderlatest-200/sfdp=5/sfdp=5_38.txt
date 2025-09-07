
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(128, 512)
 
    def forward(self, qk):
        attn_weight = torch.softmax(qk, dim=-1)
        attn_weight = torch.dropout(attn_weight, dropout_p, True)
        output = attn_weight @ v
        return output


# Initializing the model
m = Model()

# Inputs to the model
qk  = torch.randn(256, 1024, 128, 30)
