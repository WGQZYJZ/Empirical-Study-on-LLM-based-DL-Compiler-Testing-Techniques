
class Model(torch.nn.Module):
    def __init__(self, size=9223372036854775807)
        super().__init__()
 
    def forward(self, t1, t2):
        v1  = torch.cat([t1, t2], dim=1)
        v2  = v1[:, 0:size]
        return v2


# Initializing the model with different input size to meet requirements
m  = Model(384)
 
# Input tensors to the model
x1 = torch.randn(2, 576)
x2 = torch.randn(2, 90 * 384 - 576)


__output__  = m(x1, x2)

