
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1, x2):
        t1 = x1.permute(0, 3, 1, 4) # permute the input tensor A
        t2 = x2.permute(0, 3, 1, 5) # permute the input tensor B
        v1  = torch.bmm(t1, t2) 
        return v1

# Initializing the model