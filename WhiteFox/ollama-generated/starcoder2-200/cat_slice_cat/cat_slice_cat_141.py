
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        v1 = torch.cat([x1] * 30)
        v2 = v1[:, 0:9223372036854775807].clone()
        v3 = v2[:, 0:size] 
        v4 = torch.cat(v1, v3, dim=1).clone()
        return v4


# Initializing the model
m = Model()

# Inputs to the model
__input1__ = torch.randn([batch_size_, 5760, 89])
__input2__ = torch.randn([30 * batch_size_, 10, 5760])
__output__  = m(__input1__, __input2__)

