
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(32, 8)
 
    def forward(self, x1, x2, query=None, key=None, scale_factor=None, dropout_p=0.5):
        