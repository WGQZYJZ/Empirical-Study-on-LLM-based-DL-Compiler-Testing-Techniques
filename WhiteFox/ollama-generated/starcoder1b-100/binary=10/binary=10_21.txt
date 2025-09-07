
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(3, 8)
 
    def forward(self, x1):
        v1 = self.linear(x1) + torch.randn(10, 5, device=x1.device)
        return v1


# Initializing the model
m = Model()
m.load_state_dict({'linear.weight': torch.randn(8, 3).cuda(), 'linear.bias': torch.randn(8).cuda(), 'linear2.bias': torch.randn(8).cuda()})

