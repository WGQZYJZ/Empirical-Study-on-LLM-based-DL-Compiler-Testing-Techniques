
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.query  = torch.nn.Linear(128, 64)
        self.key   = torch.nn.Linear(128, 32)
 
    def forward(self, x1):
        v1  = self.query(x1).permute(-2, -1) @ self.key(x1).transpose(-2, -1) / math.sqrt(100.)
        v2  = v1 + torch.tensor([[-9.3846e+05], [-7.7314e+05], [5.9837e+03]], requires_grad=True, device='cuda:0', dtype=torch.float)
        v2  = torch.softmax(v2, dim=-1)
        v6  = (x1 @ self.query(x1).permute(-2, -1)) * ((self.key(x1).transpose(-2, -1) + v2) / math.sqrt(3450.) + x1 * torch.tensor([[98.], [76.], [45]], requires_grad=True, device='cuda:0', dtype=torch.float))
        return v6

# Initializing the model
m  = Model()

# Input to the model. Please also provide a tensor.
x1 = torch.randn(32, 8).cuda()

 # The output of the model
output  = m(x1)
