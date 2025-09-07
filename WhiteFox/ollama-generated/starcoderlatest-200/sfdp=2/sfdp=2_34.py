
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.query = torch.nn.Conv2d(3, 8, 1, stride=1, padding=0)
        self.key   = torch.nn.Conv2d(3, 8, 1, stride=1, padding=0)
 
    def forward(self, qk):
        softmax_qk  = qk.softmax(dim=-1)
        output  = softmax_qk.matmul(value)
        return output
 
 # Initializing the model
m = Model()

 # Inputs to the model
qk  = torch.randn(1024, 3, 64, 64)
