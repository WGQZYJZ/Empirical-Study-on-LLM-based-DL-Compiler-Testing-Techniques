
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.scale = 1 / (8 * 8)
 
    def forward(self, qk):
        vq  = torch.matmul(qk, qk.transpose(-2, -1)) 
        vs  = vq.div(self.scale)
        vo  = vs.softmax(dim=-1).mul_(vk)
        return vo

# Initializing the model
m  = Model()

 # Inputs to the model
q   = torch.randn(32, 640, 8, 8)
k   = torch.randn(32, 640, 8, 8)
__output__    = m(torch.matmul(q, k))

