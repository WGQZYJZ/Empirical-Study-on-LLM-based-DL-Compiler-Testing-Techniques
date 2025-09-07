
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
        self.linear = torch.nn.Linear(1024, 5)
 
    def forward(self, x1):

        v76 = torch.randn(32, 1024).to(x1.device)
        v78 = torch.randn(32, 5).to(x1.device)
 
        v79 = self.linear(v76)

        