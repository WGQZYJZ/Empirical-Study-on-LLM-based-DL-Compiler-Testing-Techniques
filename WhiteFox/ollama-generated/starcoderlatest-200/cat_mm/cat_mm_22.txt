
class Model(torch.nn.Module):
    def __init__(self, input_dim):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(input_dim, 8, 3, stride=2, padding=1)
 
    def forward(self, x1, x2):
        v1 = self.conv1(x1)
        t1 = torch.mm(v1, x2)
        v2 = torch.cat([t1, t1], dim=0)
        return v2


# Initializing the model and obtaining the input tensors of model
m = Model(3)
__input_tensor1__ = x1
__input_tensor2__ = x2

