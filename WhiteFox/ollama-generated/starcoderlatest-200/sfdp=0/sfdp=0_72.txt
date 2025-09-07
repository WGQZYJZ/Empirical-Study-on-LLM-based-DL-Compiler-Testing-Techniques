
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.key = torch.nn.Parameter(torch.randn(256, 512), requires_grad=True)
 
    def forward(self, q):
        attn_weights = torch.matmul(q, self.key.transpose(-2, -1)) / math.sqrt(float(q.shape[-1]))
        return attn_weights.softmax(dim=-1)

 # Initializing the model
m = Model()
 
 # Inputs to the model
 x  = torch.randn(2048, 512, 32, 16)
 