
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, x2):
        v1  = torch.softmax(x1 @ x2.transpose(-2, -1) / math.sqrt(x1.size(-1)), dim=-1)
        return (v1 @ x2 + x1)


# Initializing the model<|end_of_model|>
m  = Model()
 
 
 # Inputs to the model<|end_of_model|>
 x1 = torch.randn(3, 8000, 4096)
 x2 = torch.randn(3, 512, 768)
 __output__  = m(x1, x2)