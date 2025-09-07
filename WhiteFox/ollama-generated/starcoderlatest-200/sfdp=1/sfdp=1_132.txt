
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attn_layer  = torch.nn.Linear(512, 3072)
        self.query       = torch.nn.Linear(512, 128, bias=False)
        self.value       = torch.nn.Linear(512, 128, bias=False)
 
    def forward(self, x1):
        v1 = torch.tanh(self.attn_layer(x1))
        query = self.query(v1)
        key   = self.key(v1)
        # scaled_qk  = qk.div(inv_scale_factor) # Scale the dot product by the inverse scale factor
        softmax_qk = torch.softmax(torch.matmul(query, key.transpose(-2, -1)) / 3072., dim=-1)
        output     = torch.matmul(dropout_qk, value)
        return v6
# Initializing the model
m = Model()


def generateInputTensorForModel():
    