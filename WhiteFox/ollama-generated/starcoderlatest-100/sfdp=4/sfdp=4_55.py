
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(128, 64)
 
    def forward(self, qk, attn_mask, value):
        v = self.linear(qk) * math.sqrt(attn_mask.size(-1))
        return (v + attn_mask * value).sum((2, 3), keepdim=True)
 
 # Initializing the model
m = Model()

 # Inputs to the model
 x_q = torch.randn(5, 64, 128)
 x_k = torch.randn(10, 64, 128)
 x_v = torch.randn(10, 64, 128)
 attn_mask = torch.arange(64).view(1, -1).repeat((1, 128))
 