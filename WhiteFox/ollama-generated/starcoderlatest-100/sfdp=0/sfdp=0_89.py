
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.fc1 = torch.nn.Linear(3072, 8)
 
    def forward(self, x1):
        v1 = torch.einsum('ncj->nj', x1).reshape(x1.shape[0], -1)
        