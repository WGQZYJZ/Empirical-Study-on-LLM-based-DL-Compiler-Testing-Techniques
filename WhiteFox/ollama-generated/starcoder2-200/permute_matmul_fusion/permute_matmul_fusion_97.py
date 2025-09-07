
class Model(torch.nn.Module):
    def __init__(self, B):
        super().__init__()

    def forward(self, x1, x2):
        v1  = x1.permute(0, 3, 1) # Permute the input tensor A
        v2  = x2.permute(0, 3, 1) # Permute the input tensor B
        t_a  = torch.bmm(v1, v2)
        t_b  = torch.bmm(v2, v1)

# Initializing the model
m  = Model(2)

