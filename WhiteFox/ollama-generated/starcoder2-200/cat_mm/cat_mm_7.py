
class Model(torch.nn.Module):
    def __init__(self, in1: torch.Tensor, in2: torch.Tensor):
        super().__init__()
        self.matmul  = torch.mm
 
    def forward(self, x3):
        v0  = self.matmul(x3[0], x3[1])
[0:v0.shape[0]][0:v0.shape[-1]]  = v0  * v0.sum(dim=1)
[v0.shape[0]:v0.shape[0]+len(x3)][0]  = x3[2].repeat((self.matmul(x3, torch.Tensor([v0.max()])), 1))
v6  = [v0.shape[0]+len(x3)]
        return v0.sum(dim=int(len(x3)))


# Initializing the model
m = Model(torch.randn(4, 5).requires_grad_(True), torch.randn(2, 1).requires_grad_(True))

# Inputs to the model
x1  = [torch.randn(800, 30) for _ in range(4)]

