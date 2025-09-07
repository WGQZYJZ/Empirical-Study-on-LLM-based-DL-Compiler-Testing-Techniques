

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.scale = torch.nn.Parameter(torch.tensor([0.9]))
 
    def forward(self, q1, k2):
        v2  = self.scale * (q1 @ k2).transpose(-2, -1)
        return softmax_qk

# Initializing the model
m  = Model()

 # Inputs to the model
q1 = torch.randn(30528, 768)
k2 = torch.randn(30528, 768)
 
